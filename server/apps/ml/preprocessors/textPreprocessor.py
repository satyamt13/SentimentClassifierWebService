import numpy as np
import re
import json
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import split_alphanum
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_tags

CONTRACTION_DICT = {}

class textPreprocessor:

    def lowerCase(self,string):
        return string.lower()

    def createContractions(self):
        return re.compile('(%s)' % '|'.join(CONTRACTION_DICT.keys()))

    def replaceWith(self,match):
        return CONTRACTION_DICT[match.group(0)]

    def expandContractions(self,string):
        pass










