import psycopg2

class DatabaseConnection:

    def __init__(self):
        params = {
            'database': '',
            'user': '',
            'password': '',
            'host': '',
            'port': 5432,
        }

        self.conn = psycopg2.connect(**params)