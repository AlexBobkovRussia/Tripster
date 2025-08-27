from .main_db import Database


class AuthDB(Database):
    def signup(self, username: str, password: str, email: str):
        with self._conn.cursor() as conn:
            result = conn.execute(
                f"""
SELECT username, password, email
FROM users
WHERE username = {username} OR password = {password} OR email = {email}
                """
            )
            if result:
                return False
            result = conn.execute(
                f"""
INSERT INTO users VALUES(username, password, email)
({username}, {password}, {email});
                """
            )
        return result

    def login(self, username: str, password: str):
        with self._conn.cursor() as conn:
            result = conn.execute(
                f"""
SELECT username, password
FROM users
WHERE username = {username} AND password = {password};
                """
            )
        return result

    def me(self, username: str, password: str):
        with self._conn.cursor() as conn:
            pass


if __name__ == "__main__":
    db = Database(
        user="postgres",
        password="Gq-Rpa7{jr]!@pr",
        database="Tripster",
        host="127.0.0.1",
        port=5432,
    )
