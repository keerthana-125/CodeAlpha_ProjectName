# flashcard_manager.py

import json
import os

class FlashcardManager:
    def __init__(self, filename="flashcard_data.json"):
        self.filename = filename
        self.flashcards = []
        self.load_flashcards()

    def load_flashcards(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.flashcards = json.load(f)
        else:
            self.flashcards = []

    def save_flashcards(self):
        with open(self.filename, "w") as f:
            json.dump(self.flashcards, f, indent=2)

    def add_flashcard(self, question, answer):
        self.flashcards.append({"question": question, "answer": answer})
        self.save_flashcards()

    def edit_flashcard(self, index, new_question, new_answer):
        if 0 <= index < len(self.flashcards):
            self.flashcards[index] = {"question": new_question, "answer": new_answer}
            self.save_flashcards()

    def delete_flashcard(self, index):
        if 0 <= index < len(self.flashcards):
            del self.flashcards[index]
            self.save_flashcards()
