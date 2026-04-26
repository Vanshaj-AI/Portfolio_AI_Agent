import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def execute_query(self, query: str, params=None) -> pd.DataFrame:
        return pd.read_sql(query, self.conn, params=params)

    def execute_script(self, script_path: str):
        with open(script_path, "r") as f:
            self.conn.executescript(f.read())

    def close(self):
        self.conn.close()