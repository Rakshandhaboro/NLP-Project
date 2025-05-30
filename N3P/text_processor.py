import string
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
    
    def clean_text(self, text):
        """Basic text cleaning"""
        text = text.lower().strip()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text
    
    def remove_stopwords(self, tokens):
        """Filter out stopwords"""
        return [word for word in tokens if word not in self.stopwords]
    
    def normalize(self, text):
        """Complete text normalization pipeline"""
        from .tokenizer import Tokenizer  # Local import to avoid circular dependencies
        text = self.clean_text(text)
        tokens = Tokenizer().word_tokenize(text)
        return self.remove_stopwords(tokens)
