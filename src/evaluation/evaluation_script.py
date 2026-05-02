import sys
import os
import json
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.database_manager import DatabaseManager
from data.schema_manager import SchemaManager
from llm.gemini_client import GeminiClient
from tools.sql_generator import SQLTool
from tools.sector_exposure_calculator import ExposureTool
from agent.portfolio_ai_agent import PortfolioAgent
from core.config import Config


class GroundTruthEvaluator:
    def __init__(self, ground_truth_path: str):
        self.db = DatabaseManager(Config.DB_FILE)
        self.schema = SchemaManager(self.db)
        self.llm = GeminiClient()

        self.sql_tool = SQLTool(self.llm, self.schema, self.db)
        self.exposure_tool = ExposureTool(self.db)

        self.agent = PortfolioAgent(
            self.llm,
            self.sql_tool,
            self.exposure_tool
        )

        with open(ground_truth_path, "r") as f:
            self.test_cases = json.load(f)["questions"]

    def normalize_result(self, df):
        if isinstance(df, pd.DataFrame):
            return df.astype(str).values.tolist()
        return df

    def evaluate_text2sql(self, question, ground_truth_sql):
        generated_sql = self.sql_tool.generate_sql(question).replace('`', '').replace('sql', '')
        print("GENERATED SQL:", generated_sql)
        expected_result = self.db.execute_query(ground_truth_sql)
        generated_result = self.db.execute_query(generated_sql)

        sql_match = generated_sql.strip().lower() == ground_truth_sql.strip().lower()

        result_match = (
            self.normalize_result(expected_result)
            == self.normalize_result(generated_result)
        )

        return {
            "question": question,
            "generated_sql": generated_sql,
            "ground_truth_sql": ground_truth_sql,
            "sql_match": sql_match,
            "result_match": result_match
        }

    def run_all_tests(self):
        results = []

        for case in self.test_cases:
            if case["type"] == "text2sql":
                result = self.evaluate_text2sql(
                    case["question"],
                    case["ground_truth"]["sql_query"]
                )
                results.append(result)

        return pd.DataFrame(results)


if __name__ == "__main__":
    ground_truth_file = os.path.join(
        os.path.dirname(__file__),
        "ground_truth.json"
    )

    evaluator = GroundTruthEvaluator(ground_truth_file)

    results_df = evaluator.run_all_tests()

    print(results_df)

    accuracy = results_df["result_match"].mean() * 100
    print(f"\nOverall Accuracy: {accuracy:.2f}%")