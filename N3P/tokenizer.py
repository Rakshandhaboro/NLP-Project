import re
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

class Tokenizer:
    def tokenize(self, text):
        return word_tokenize(text.lower())
