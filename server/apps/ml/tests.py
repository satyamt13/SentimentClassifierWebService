from django.test import TestCase
from apps.ml.sentimentClassifier.CLSTM import CLSTM
import inspect
from apps.ml.registry import MlRegistry
'''
Quick sanity test for the API and the model using and in the vocabulary input 
'''
class MlTests(TestCase):
    def test_model(self):
        input_data = {
            "text": """"I have to admit that I am a fan of Giada's cooking and I had great expectations when I ordered this set. 
            They were however, crushed. While I still love Giada's cooking, this set is just a way for Food Network to 
            make money. They really cheated with these DVD's. All they have are the video from the show, no text recipes, 
            no link to the on line shows and no computer support. They play in Windows media player but the set does not 
            contain the recipes. You can get more by taping the shows and then going to the web to download recipes. 
            Another disappointment is the so so transfer quality to DVD. Perhaps I've been spoiled by HD and Tivo but the 
            older shows I've recorded have had better playback quality than the episodes on the DVD's. 
            It is in the old 480p but the quality of the transfer to DVD is dark and about the same quality as 
            your average old VHS tape, not DVD quality. I get the impression Food Network got cheap and subbed out 
            the DVD transfer to the lowest bidder (China?) and it shows.I could watch Giada read the dictionary and 
            her cooking is really first rate. But, that's all you get is watching Giada. Thank god she is easy to 
            understand and her recipes are easy to follow. But to get consistent results on some of the dishes, 
            you should search the web and find the hard copies.  While Giada herself is great, this set is a waste of money. 
            You're better off recording the shows and going to the web to get the recipes you want or, better yet, 
            just stick with her cookbooks which are all first rate and worlds above this cheap presentation.Don't waste your money"""
        }
        my_alg = CLSTM()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual("OK", response["Status"])
        self.assertTrue("Label" in response)
        self.assertTrue("Positive" in response)
        self.assertTrue("Neutral" in response)
        self.assertTrue("Negative" in response)
        print(response)

    def test_registry(self):
        registry = MlRegistry()
        self.assertEqual(len(registry.endpoints),0)
        endpoint_name = "sentiment_classifier"
        algorithm_object = CLSTM()
        algorithm_name = "CLSTM"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Luci4"
        algorithm_description = """C-LSTM(Zhou Et al. 2015) sentiment classifier with Phrases2Vec embedding layer
         trained on over 1 million Amazon movies & T.V. reviews"""
        algorithm_code = inspect.getsource(CLSTM)
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                               algorithm_status, algorithm_version, algorithm_owner,
                               algorithm_description, algorithm_code)
        self.assertEqual(len(registry.endpoints), 1)









