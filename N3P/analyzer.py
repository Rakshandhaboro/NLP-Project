from .processor import TextProcessor
from .techniques import Tokenizer

class TextAnalyzer(TextProcessor):
    def __init__(self):
        super().__init__()
        self.tokenizer = Tokenizer()
    
    def analyze_sentiment(self, text):
        """Basic sentiment analysis (placeholder implementation)"""
        normalized = self.normalize(text)
        # In a real implementation, you would add sentiment analysis logic here
        return {"sentiment": "neutral", "score": 0.0}
    
    def get_keywords(self, text, top_n=5):
        """Extract top keywords (placeholder implementation)"""
        tokens = self.tokenizer.word_tokenize(text)
        return tokens[:top_n]
