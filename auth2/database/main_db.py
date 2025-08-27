import psycopg2
from passlib.context import CryptContext

pwd_context = CryptContext(shemes={"bcrypt"}, deprecated="auto")


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

    def __enter__(self):
        return self._conn

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def close(self):
        self._conn.close()
