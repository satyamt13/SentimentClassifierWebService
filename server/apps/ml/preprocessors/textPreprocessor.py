import re
import json
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import split_alphanum
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_tags
from gensim.models.phrases import Phraser
import os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
'''
text preprocessor class that applies all preprocessing steps to raw input 
before it can be passed to the model. It uses two static files associated with 
expanding contractions and the phrases model.
'''
class textPreprocessor:

    with open(os.path.join(CURRENT_PATH, "../../artifacts/contractions_mapping.json")) as jsonFile:
        CONTRACTION_MAPPING = json.load(jsonFile)

    COMPILED_RE = re.compile('(%s)' % '|'.join(CONTRACTION_MAPPING.keys()))

    PHRASES_MODEL = Phraser.load(os.path.join(CURRENT_PATH, "../../artifacts/phrases_model.pkl"))

    def lower_case(self, string):
        return string.lower()
    '''
    Methods that use RE and a JSON mapping file to expand and replace all 
    contractions , don't -> do not which is later picked up by the phrases model 
    and converted to one token -> do_not
    '''
    def replace_with(self, match):
        return self.CONTRACTION_MAPPING[match.group(0)]

    def expand_contractions(self, string):
        return self.COMPILED_RE.sub(self.replace_with, string)
    '''
    Applies all Gensim preprocessors, our custom ones as well as the trained 
    Gensim phrases model for the Phrases2Vec embedding layer in the CLSTM model 
    to be useful 
    '''
    def preprocess(self, string):
        preprocessed_tokenized_string = preprocess_string(string, filters=[self.lower_case,
                                                                           self.expand_contractions,
                                                                           split_alphanum,
                                                                           strip_multiple_whitespaces,
                                                                           strip_non_alphanum, strip_numeric,
                                                                           strip_tags,
                                                                           strip_punctuation])
        return self.PHRASES_MODEL[preprocessed_tokenized_string]
















