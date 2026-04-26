import ast
import re

class PortfolioAgent:
    def __init__(self, llm_client, sql_tool, exposure_tool):
        self.llm = llm_client
        self.sql_tool = sql_tool
        self.exposure_tool = exposure_tool

    def choose_tool(self, user_query: str):
        prompt = f"""
        You are an AI agent.
            
            Decide which tool to use:
            
            1. sql_tool → for database queries (counts, lists, filters, etc.)
            2. exposure_tool → for portfolio sector exposure calculations
            
            Return ONLY one:
            - sql_tool
            - exposure_tool

            Additionally Extract portfolio_id from the user query. 
            Output Format = tool_name, portfolio_id = [list_of_ids]
        
            Query: {user_query}
        """

        return self.llm.generate(prompt)

    def run(self, user_query: str):
        output = self.choose_tool(user_query)
        tool = output.split(",")[0].strip()

        match = re.search(r'\[.*?\]', output)
        portfolio_ids = ast.literal_eval(match.group()) if match else []

        if tool == "sql_tool":
            return self.sql_tool.run(user_query)

        elif tool == "exposure_tool":
            return self.exposure_tool.calculate_sector_exposure(portfolio_ids)

        raise ValueError("Unsupported query type")