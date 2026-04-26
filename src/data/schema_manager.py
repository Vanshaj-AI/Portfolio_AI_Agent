class SchemaManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_schema(self):
        cursor = self.db_manager.conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """)

        schema = {}
        for (table_name,) in cursor.fetchall():
            cursor.execute(f"PRAGMA table_info({table_name});")
            schema[table_name] = [col[1] for col in cursor.fetchall()]

        return schema

    @staticmethod
    def format_schema(schema_dict):
        return "\n".join(
            f"Table: {table}\nColumns: {', '.join(cols)}"
            for table, cols in schema_dict.items()
        )