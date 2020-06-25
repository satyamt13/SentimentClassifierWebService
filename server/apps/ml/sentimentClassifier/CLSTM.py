from apps.ml.preprocessors.textPreprocessor import textPreprocessor
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import json
from keras_preprocessing.text import tokenizer_from_json

class CLSTM:
    def __init__(self):
        self.preprocessor = textPreprocessor()
        self.model = load_model("/Users/sam/Documents/project_reboot/c_lstm_reduced.h5")
        self.model._make_predict_function()
        with open("/Users/sam/Documents/project_reboot/keras_tokenizer.json") as f:
            data = json.load(f)
            self.tokenizer = tokenizer_from_json(data)

    def preprocessing(self, inputData):
        return [self.preprocessor.preprocess(inputData["text"])]

    def encode_tokenize_pad(self, preprocessed_input_data):
        tokenized_input_data = self.tokenizer.texts_to_sequences(preprocessed_input_data)
        return pad_sequences(tokenized_input_data, maxlen=100, padding="pre", truncating="pre")

    def predict(self, padded_tokenized_input_data):
        return self.model.predict_proba(padded_tokenized_input_data)

    def postprocessing(self, probability_vector, labels=["Negative", "Neutral", "Positive"]):
        return {
            "Label": labels[np.argmax(probability_vector)],
            "Negative": probability_vector[0],
            "Neutral": probability_vector[1],
            "Positive": probability_vector[2],
            "Status": "OK"
        }

    def compute_prediction(self, inputData):
        try:
            preprocessed_input_data = self.preprocessing(inputData)
            encoded_padded_input_data = self.encode_tokenize_pad(preprocessed_input_data)
            probability_vector = self.predict(encoded_padded_input_data)[0]
            prediction = self.postprocessing(probability_vector)
        except Exception as e:
            return {"Status": "Error", "message": str(e)}
        return prediction

