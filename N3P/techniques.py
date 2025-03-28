from .processor import TextProcessor

class Tokenizer:
    def word_tokenize(self, text):
        """Basic word tokenizer"""
        return text.split()

class TextNormalizer(TextProcessor):
    def normalize(self, text):
        """Complete text normalization pipeline"""
        text = self.clean_text(text)
        tokens = Tokenizer().word_tokenize(text)
        return self.remove_stopwords(tokens)
