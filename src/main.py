__author__ = "Vanshaj Jain"
__version__ = "1.0.0"

from core.config import Config
from data.database_manager import DatabaseManager
from data.schema_manager import SchemaManager
from data.database_ingestion import DataIngestion
from llm.gemini_client import GeminiClient
from tools.sql_generator import SQLTool
from tools.sector_exposure_calculator import ExposureTool
from agent.portfolio_ai_agent import PortfolioAgent


def main():
    # Initialize database connection
    db = DatabaseManager(Config.DB_FILE)

    # Create database schema
    db.execute_script(Config.SCHEMA_FILE)

    # Load CSV files into database
    ingestion = DataIngestion(db, Config.CSV_FOLDER)
    ingestion.load_csvs_to_database()

    # Initialize schema manager and LLM
    schema = SchemaManager(db)
    llm = GeminiClient()

    # Initialize tools
    sql_tool = SQLTool(llm, schema, db)
    exposure_tool = ExposureTool(db)

    # Initialize agent
    agent = PortfolioAgent(llm, sql_tool, exposure_tool)

    print("📊 Portfolio AI Agent Ready")

    while True:
        query = input("You: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        try:
            result = agent.run(query)
            print(result)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()