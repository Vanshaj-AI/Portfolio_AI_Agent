import streamlit as st

from core.config import Config
from data.database_manager import DatabaseManager
from data.schema_manager import SchemaManager
from data.database_ingestion import DataIngestion
from llm.gemini_client import GeminiClient
from tools.sql_generator import SQLTool
from tools.sector_exposure_calculator import ExposureTool
from agent.portfolio_ai_agent import PortfolioAgent

st.set_page_config(page_title="Portfolio AI Agent", layout="wide")

@st.cache_resource
def initialize_agent():
    db = DatabaseManager(Config.DB_FILE)

    # Optional first-time setup
    db.execute_script(Config.SCHEMA_FILE)

    ingestion = DataIngestion(db, Config.CSV_FOLDER)
    ingestion.load_csvs_to_database()

    schema = SchemaManager(db)
    llm = GeminiClient()

    sql_tool = SQLTool(llm, schema, db)
    exposure_tool = ExposureTool(db)

    return PortfolioAgent(llm, sql_tool, exposure_tool)


agent = initialize_agent()

st.set_page_config(page_title="Portfolio AI Agent", layout="wide")

st.title("📊 Portfolio AI Agent")
st.write("Ask portfolio analytics questions using natural language.")

user_query = st.text_input("Enter your query:")

if st.button("Run Query"):
    if user_query:
        try:
            result = agent.run(user_query)

            st.success("Query executed successfully!")

            if hasattr(result, "empty"):
                st.dataframe(result)
            else:
                st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")