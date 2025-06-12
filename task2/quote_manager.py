# quote_manager.py

import json
import random

class QuoteManager:
    def __init__(self, filename="quotes.json"):
        self.filename = filename
        self.quotes = self.load_quotes()

    def load_quotes(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def get_random_quote(self):
        if self.quotes:
            return random.choice(self.quotes)
        return {"text": "No quotes found.", "author": ""}
