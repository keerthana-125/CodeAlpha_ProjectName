# main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from fitness_db import FitnessDB
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class FitnessApp:
    def __init__(self, root):
        self.db = FitnessDB()
        self.root = root
        self.root.title("Fitness Tracker Dashboard")
        self.root.geometry("750x650")
        self.root.configure(bg="white")

        # Variables
        self.date_var = tk.StringVar(value=datetime.today().strftime('%Y-%m-%d'))
        self.steps_var = tk.IntVar()
        self.workout_var = tk.IntVar()
        self.calories_var = tk.IntVar()

        # Title
        tk.Label(root, text="Fitness Track", font=("Arial", 18, "bold"), bg="white", fg="#333").pack(pady=10)

        # Form
        form = tk.Frame(root, bg="white")
        form.pack(pady=10)

        tk.Label(form, text="Select Date:", bg="white").grid(row=0, column=0, sticky="e")
        self.date_entry = DateEntry(form, textvariable=self.date_var, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1)

        tk.Label(form, text="Steps:", bg="white").grid(row=1, column=0, sticky="e")
        tk.Entry(form, textvariable=self.steps_var).grid(row=1, column=1)

        tk.Label(form, text="Workout (min):", bg="white").grid(row=2, column=0, sticky="e")
        tk.Entry(form, textvariable=self.workout_var).grid(row=2, column=1)

        tk.Label(form, text="Calories:", bg="white").grid(row=3, column=0, sticky="e")
        tk.Entry(form, textvariable=self.calories_var).grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Log Entry", command=self.log_entry, bg="grey", fg="white").pack(pady=10)
        tk.Button(root, text="Show Weekly Report", command=self.show_weekly_report, bg="purple", fg="white").pack(pady=5)
        # Report Table
        self.report_table = ttk.Treeview(root, columns=("Date", "Steps", "Workout", "Calories"), show="headings")
        for col in ("Date", "Steps", "Workout", "Calories"):
            self.report_table.heading(col, text=col)
            self.report_table.column(col, width=150, anchor="center")
        self.report_table.pack(pady=10, fill="x")

        # Summary Label
        self.summary_label = tk.Label(root, text="", bg="white", font=("Arial", 12))
        self.summary_label.pack(pady=5)

    def log_entry(self):
        try:
            date_str = self.date_var.get()
            datetime.strptime(date_str, '%Y-%m-%d')
            self.db.add_entry_with_date(
                date_str,
                self.steps_var.get(),
                self.workout_var.get(),
                self.calories_var.get()
            )
            messagebox.showinfo("Success", f"Entry for {date_str} logged successfully!")
            self.clear_inputs()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_inputs(self):
        self.steps_var.set(0)
        self.workout_var.set(0)
        self.calories_var.set(0)

    def show_weekly_report(self):
        try:
            selected_date = datetime.strptime(self.date_var.get(), '%Y-%m-%d')
            monday = selected_date - timedelta(days=selected_date.weekday())
            sunday = monday + timedelta(days=6)
            data = self.db.get_entries_between(monday.strftime('%Y-%m-%d'), sunday.strftime('%Y-%m-%d'))

            self.report_table.delete(*self.report_table.get_children())

            total_steps = total_workout = total_calories = 0

            for row in data:
                self.report_table.insert("", "end", values=row)
                total_steps += row[1] or 0
                total_workout += row[2] or 0
                total_calories += row[3] or 0

            self.summary_label.config(
                text=f"Weekly Total - Steps: {total_steps}, Workout: {total_workout} min, Calories: {total_calories}"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()
