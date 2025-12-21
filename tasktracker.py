"""
Logic for the task tracker cli.
"""
import sqlite3
from datetime import date

class TaskTracker:
    """
    Object to hold methods for the task tracker cli.
    """
    def __init__(self, database: str, table: str):
        """
        Initialize TaskTracker object.

        Parameters:
            database (str): database name
            table (str): table name
        """
        self.__database = database
        self.__table = table
        self.__connection = sqlite3.connect(self.__database)
        self.__cursor = self.__connection.cursor()
    def check(self) -> bool:
        """
        Method used to make sure the database and table exists.

        Returns:
            True
        """
        self.__cursor.executescript(f"""
        BEGIN;
        CREATE TABLE IF NOT EXISTS {self.__table} (
            task_name TEXT,
            due_date DATE,
            complete BOOLEAN,
            UNIQUE(task_name, due_date)
        );
        COMMIT;
        """)
        return True
    def list_task(self, complete: bool = False) -> list[tuple[str, date, bool]]: # return list of tuples
        """
        List tasks in the database base on complete or not.

        Parameters:
            complete (bool):
        
        Returns:
            list: list of (tasks, date, complete)
        """
        list_task_sql = f"SELECT * FROM '{self.__table}'"
        return self.__cursor.execute(list_task_sql).fetchall()
    def add(self, task: str, due_date: date = date.today()) -> None:
        """
        Add task to database.

        Parameters:
            task (str): name of the task.
            due_date (datetime): due date of the task. Defaults to today.
        
        Returns:
            None
        """
        add_sql = f"INSERT OR IGNORE INTO {self.__table} VALUES('{task}','{due_date}',{int(False)})"
        self.__cursor.execute(add_sql)
        self.__connection.commit()
    def complete(self,
            task: str,
            due_date: date= date.today(),
            complete: bool = True
            ) -> None:
        """
        Complete tasks in the database.

        Parameters:
            task (str): name of the task.
            due_date (datetime): due date of the task. Defaults to today.
            complete (bool): Defaults to True.

        Returns:
            None
        """
        complete_sql = f"UPDATE OR IGNORE {self.__table}\
                        SET complete={int(complete)}\
                        WHERE task_name='{task}' AND due_date='{due_date}'"
        self.__cursor.execute(complete_sql)
        self.__connection.commit()
    def close(self):
        """
        Commits and closes the connection to the database.
        """
        self.__connection.commit()
        self.__connection.close()
