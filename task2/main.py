# main.py

import tkinter as tk
from quote_manager import QuoteManager

class QuoteApp:
    def __init__(self, root):
        self.manager = QuoteManager()
        self.root = root
        self.root.title("Random Quote Generator")
        self.root.geometry("600x300")
        self.root.configure(bg="white")

        self.quote_label = tk.Label(
            root,
            text="",
            font=("Calibri", 14, "italic"),
            wraplength=500,
            justify="center",
            bg="white",
            fg="#555"
        )
        self.quote_label.pack(pady=30)

        self.author_label = tk.Label(
            root,
            text="",
            font=("Helvetica", 12, "bold"),
            fg="#333",
            bg="white"
        )
        self.author_label.pack()

        self.new_quote_btn = tk.Button(
            root,
            text="New Quote",
            command=self.show_quote,
            bg="#008CBA",
            fg="white",
            font=("Arial", 12),
            padx=15,
            pady=5,
            cursor="hand2"
        )
        self.new_quote_btn.pack(pady=20)

        self.show_quote()  # show one at launch

    def show_quote(self):
        quote = self.manager.get_random_quote()
        self.quote_label.config(text=f'"{quote["text"]}"')
        self.author_label.config(text=f"- {quote['author']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
