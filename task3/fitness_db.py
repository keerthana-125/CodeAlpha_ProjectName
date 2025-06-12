# fitness_db.py

import sqlite3

class FitnessDB:
    def __init__(self, db_name="fitness.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS fitness (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_date TEXT NOT NULL,
            steps INTEGER DEFAULT 0,
            workout_time INTEGER DEFAULT 0,
            calories INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()

    def add_entry_with_date(self, log_date, steps, workout_time, calories):
        self.conn.execute(
            "INSERT INTO fitness (log_date, steps, workout_time, calories) VALUES (?, ?, ?, ?)",
            (log_date, steps, workout_time, calories)
        )
        self.conn.commit()

    def get_entries_between(self, start_date, end_date):
        cursor = self.conn.execute("""
        SELECT log_date, SUM(steps), SUM(workout_time), SUM(calories)
        FROM fitness
        WHERE log_date BETWEEN ? AND ?
        GROUP BY log_date
        ORDER BY log_date ASC
        """, (start_date, end_date))
        return cursor.fetchall()
