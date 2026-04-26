class ExposureTool:
    def __init__(self, db_manager):
        self.db = db_manager

    def calculate_sector_exposure(self, portfolio_ids):
        placeholders = ",".join(["?"] * len(portfolio_ids))

        query = f"""
        WITH holdings_grouped AS (
            SELECT portfolio_id, holding_id, security_id,
                   SUM(current_weight) AS current_weight
            FROM holdings
            WHERE portfolio_id IN ({placeholders})
            GROUP BY portfolio_id, holding_id, security_id
        ),
        joined_table AS (
            SELECT h.*, CAST(s.sector_id AS INTEGER) AS sector_id
            FROM holdings_grouped h
            LEFT JOIN securities s
              ON s.security_id = h.security_id
            WHERE asset_type != 'Bond'
        )
        SELECT j.portfolio_id,
               SUM(j.current_weight) AS sector_exposure,
               s.sector_name
        FROM joined_table j
        LEFT JOIN sectors s
          ON s.sector_id = j.sector_id
        GROUP BY portfolio_id, sector_name
        """

        return self.db.execute_query(query, params=portfolio_ids)