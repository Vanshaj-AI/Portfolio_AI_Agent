import os
import pandas as pd


class DataIngestion:
    def __init__(self, db_manager, csv_folder: str):
        self.db = db_manager
        self.csv_folder = csv_folder

    def load_csvs_to_database(self):
        for file in os.listdir(self.csv_folder):
            if file.endswith(".csv"):
                table_name = file.replace(".csv", "")
                file_path = os.path.join(self.csv_folder, file)

                df = pd.read_csv(file_path)

                df.to_sql(table_name, self.db.conn, if_exists="replace", index=False)

                print(f"Loaded {file} into {table_name}")

        self.db.conn.commit()
        print("Database is ready")