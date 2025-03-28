import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

class Tokenizer:
    def __init__(self):
        self.pattern = r'\w+'
    
    def tokenize(self, text, method='regex'):
        text = text.lower()
        if method == 'regex':
            return re.findall(self.pattern, text)
        elif method == 'nltk':
            return word_tokenize(text)
        return text.split()
