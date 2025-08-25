from passlib.context import CryptContext

from src.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = {"Alex": {"username": "Alex", "hashed_password": "$2b$12$3s5jvXf1ukpmJua2e.I.t.JxyJTE.DSbsQ8FlenbyGm2Cq285Sfy2",
               "email": "bobkovalex.yaundex.ru@yandex.ru"}}


def verify_password(plaintext_password, hashed_password):
    return pwd_context.verify(plaintext_password, hashed_password)


def authenticate_user(username: str, password: str):
    # TODO: Create a connection to db
    if not db.get(username):
        return False
    user = User(**db.get(username))
    if not verify_password(password, user.hashed_password):
        return False
    return user
