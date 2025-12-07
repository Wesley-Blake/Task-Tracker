class TaskTracker:
    def add_task(self, task: str):
        pass
    def remove_task(self, task: str):
        pass
    def list_tasks(self):
        pass

if __name__ == "__main__":
    try:
        import sqlite3
    except:
        print("Failed to import sqlite3.")
        exit()

    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    test = cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table'
        AND name='taskTable'; """).fetchall()
    if len(test) == 0:
        cursor.execute("CREATE TABLE taskTable (task, date, complete)")
        cursor.execute("""
            INSERT INTO taskTable VALUES
                ('dishes', 2025-12-6, false),
                ('laundry', 2025-12-8, false)
        """)

    for result in cursor.execute("SELECT task, date, complete FROM taskTable"):
        print(result)

    connection.commit()
    connection.close()