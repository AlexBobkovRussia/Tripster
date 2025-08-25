import psycopg2


class Database:
    def __init__(self,
                 user: str,
                 password: str,
                 database: str,
                 host: str,
                 port: int
                 ):
        self._conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def create(self, table_name):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def __enter__(self):
        return self._conn

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def close(self):
        self._conn.close()


if __name__ == "__main__":
    db = Database(
        user="postgres",
        password="Gq-Rpa7{jr]!@pr",
        database="Tripster",
        host="127.0.0.1",
        port=5432,
    )
