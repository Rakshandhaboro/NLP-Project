from collections import Counter

class Analyzer:
    def __init__(self):
        self.counter = Counter()
    
    def analyze(self, tokens):
        self.counter.update(tokens)
        return self.counter.most_common()
