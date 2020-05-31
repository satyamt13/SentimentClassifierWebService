import re
import json
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import split_alphanum
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_tags

class textPreprocessor:
    with open("../../artifacts/contractions_mapping.json") as jsonFile:
        CONTRACTION_MAPPING = json.load(jsonFile)
    COMPILED_RE = re.compile('(%s)' % '|'.join(CONTRACTION_MAPPING.keys()))

    def lowerCase(self, string):
        return string.lower()

    def replaceWith(self, match):
        return self.CONTRACTION_MAPPING[match.group(0)]

    def expandContractions(self, string):
        return self.COMPILED_RE.sub(self.replaceWith, string)

    def preprocess(self, string):
        return ' '.join(preprocess_string(string, filters=[self.lowerCase, self.expandContractions, split_alphanum,
                                                   strip_multiple_whitespaces, strip_non_alphanum, strip_numeric,
                                                   strip_tags, strip_punctuation]))















