# main.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from task1.flashcard_manager import FlashcardManager

class FlashcardApp:
    def __init__(self, root):
        self.manager = FlashcardManager()
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.index = 0
        self.showing_answer = False

        self.label = tk.Label(root, text="", font=("Arial", 16, "bold"), wraplength=400, height=5, width=30, anchor="center", justify="center", relief="groove")
        self.label.pack(pady=20)

        self.show_btn = tk.Button(root, text="Show Answer", font=("Helvetica", 12), fg="white", bg="green",padx=10, pady=5, relief="raised", borderwidth=3, activebackground="orange", cursor="hand2", command=self.toggle_card)
        self.show_btn.pack()

        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(pady=10)

        tk.Button(self.nav_frame, text="Previous", font=("Helvetica", 12), fg="white", bg="blue", borderwidth=3, activebackground="pink", command=self.prev_card).pack(side=tk.LEFT, padx=10)
        tk.Button(self.nav_frame, text="Next", font=("Helvetica", 12), fg="white", bg="green", borderwidth=3, activebackground="silver", command=self.next_card).pack(side=tk.LEFT, padx=10)

        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=10)

        tk.Button(self.action_frame, text="Add", command=self.add_card).pack(side=tk.LEFT, padx=10)
        tk.Button(self.action_frame, text="Edit", command=self.edit_card).pack(side=tk.LEFT, padx=10)
        tk.Button(self.action_frame, text="Delete", command=self.delete_card).pack(side=tk.LEFT, padx=10)

        self.display_card()

    def display_card(self):
        if not self.manager.flashcards:
            self.label.config(text="No flashcards available.")
            return

        card = self.manager.flashcards[self.index]
        text = card['answer'] if self.showing_answer else card['question']
        self.label.config(text=text)
        self.show_btn.config(text="Show Question" if self.showing_answer else "Show Answer")

    def toggle_card(self):
        self.showing_answer = not self.showing_answer
        self.display_card()

    def next_card(self):
        if self.manager.flashcards:
            self.index = (self.index + 1) % len(self.manager.flashcards)
            self.showing_answer = False
            self.display_card()

    def prev_card(self):
        if self.manager.flashcards:
            self.index = (self.index - 1) % len(self.manager.flashcards)
            self.showing_answer = False
            self.display_card()

    def add_card(self):
        question = simpledialog.askstring("Add Flashcard", "Enter question:")
        answer = simpledialog.askstring("Add Flashcard", "Enter answer:")
        if question and answer:
            self.manager.add_flashcard(question, answer)
            self.index = len(self.manager.flashcards) - 1
            self.showing_answer = False
            self.display_card()

    def edit_card(self):
        if not self.manager.flashcards:
            return
        current = self.manager.flashcards[self.index]
        question = simpledialog.askstring("Edit Flashcard", "Edit question:", initialvalue=current['question'])
        answer = simpledialog.askstring("Edit Flashcard", "Edit answer:", initialvalue=current['answer'])
        if question and answer:
            self.manager.edit_flashcard(self.index, question, answer)
            self.display_card()

    def delete_card(self):
        if not self.manager.flashcards:
            return
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this flashcard?")
        if confirm:
            self.manager.delete_flashcard(self.index)
            self.index = max(0, self.index - 1)
            self.showing_answer = False
            self.display_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
