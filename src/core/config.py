
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Config:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    DB_FILE: str = os.path.join(BASE_DIR, "exercise.db")
    SCHEMA_FILE: str = os.path.join(BASE_DIR, "data", "database_schema.sql")
    CSV_FOLDER: str = os.path.join(BASE_DIR, "data", "csv_files")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")