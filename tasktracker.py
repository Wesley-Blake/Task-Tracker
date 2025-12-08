################################################################################
#
# Object to urilize the sqlite3 library.
#
################################################################################
import sqlite3
from datetime import date, datetime

class TaskTracker:
    def __init__(self, database: str, table: str):
        # NOTE: Validate input strings.
        self.database = database
        self.table = table
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
    
    def check(self) -> bool:
        self.cursor.executescript(f"""
        BEGIN;
        CREATE TABLE IF NOT EXISTS {self.table} (
            task_name TEXT,
            due_date DATE,
            complete BOOLEAN,
            UNIQUE(task_name, due_date)
        );
        COMMIT;
        """)
        return True

    # NOTE: Add date quiry, union?
    def list_task(self, complete: bool = False) -> list: # return list of tuples
        # NOTE: Validate input
        list_task_sql = f"SELECT * FROM '{self.table}' WHERE complete={int(complete)}"
        return self.cursor.execute(list_task_sql).fetchall()
    
    def add(self, task: str, due_date: datetime = date.today()) -> None:
        # NOTE: Validate input
        add_sql = f"INSERT OR IGNORE INTO {self.table} VALUES('{task}','{due_date}',{int(False)})"
        self.cursor.execute(add_sql)
        self.connection.commit()

    def complete(self,
                task: str,
                due_date: datetime = date.today(),
                complete: bool = True
                ) -> None:
        # NOTE: Validate input
        complete_sql = f"UPDATE {self.table}\
                        SET complete={int(complete)}\
                        WHERE task_name='{task}' AND due_date='{due_date}'"
        self.cursor.execute(complete_sql)
        self.connection.commit()
    # NOTE: Commit function?
    def close():
        self.connection.commit()
        self.connection.close()