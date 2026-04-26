class SQLTool:
    def __init__(self, llm_client, schema_manager, db_manager):
        self.llm = llm_client
        self.schema_manager = schema_manager
        self.db = db_manager

    def generate_sql(self, user_query: str):
        schema_text = self.schema_manager.format_schema(
            self.schema_manager.get_schema()
        )

        prompt = f"""
        You are a SQL expert.

        Given the database schema:
        {schema_text}

        Convert the following natural language query into SQL.
        Return ONLY SQL. No explanation.

        Output Format - Strictly Only SQL query, no need to use /n or any unrequired character. A sql query that can run directly
        User Query: {user_query}
        """

        return self.llm.generate(prompt)

    def run(self, user_query: str):
        sql = self.generate_sql(user_query)
        print(f"Generated SQL: {sql}\n")
        return self.db.execute_query(sql)