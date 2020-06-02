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

class textPreprocessor:
    with open("../../artifacts/contractions_mapping.json") as jsonFile:
        CONTRACTION_MAPPING = json.load(jsonFile)
    COMPILED_RE = re.compile('(%s)' % '|'.join(CONTRACTION_MAPPING.keys()))
    PHRASES_MODEL = Phraser.load("PathToModelGoesHere.pkl")

    def lower_case(self, string):
        return string.lower()

    def replace_with(self, match):
        return self.CONTRACTION_MAPPING[match.group(0)]

    def expand_contractions(self, string):
        return self.COMPILED_RE.sub(self.replace_with, string)
    #Returns tokenized review
    def preprocess(self, string):
        preprocessed_tokenized_string = preprocess_string(string, filters=[self.lower_case, self.expand_contractions, split_alphanum,
                                                   strip_multiple_whitespaces, strip_non_alphanum, strip_numeric,
                                                   strip_tags, strip_punctuation])
        return self.PHRASES_MODEL(preprocessed_tokenized_string)
















