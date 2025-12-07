# NOTE: imports sqlite3, datetime, os
import os
from datetime import date, datetime
import argparse
import sqlite3
from platform import system
from typing import Union

# NOTE: declare constants
DATE_TODAY = date.today().isoformat()

# NOTE: Create DB & Create Table
if not os.path.isfile("tasks.db"):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()
    cursor.executescript("""
        BEGIN;
        CREATE TABLE taskTable(task TEXT, due_date DATE, complete BOOLEAN);
        COMMIT;
        """)
else:
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

# NOTE: Functions to list, add, complete tasks
def add_task(task: str, date: datetime = DATE_TODAY) -> None:
    cursor.execute(f"INSERT INTO taskTable (task, due_date, complete) VALUES('{task}', '{date}', {int(False)})")
    connection.commit()
def complete_task(task: str) -> None:
    cursor.execute(f"UPDATE taskTable SET complete = {int(True)} WHERE task = '{task}'")
    connection.commit()
def list_task(date: Union[datetime, str] = DATE_TODAY, complete: bool = False) -> None:
    for result in cursor.execute(f"SELECT * FROM taskTable WHERE due_date <= '{date}' AND complete = {int(complete)}"):
        print(result)
# NOTE: Read args


# NOTE: Start testing here.
add_task("Dishes")
complete_task("Dishes")
list_task(complete=True)

# End the program
cursor.close()