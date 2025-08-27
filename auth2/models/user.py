from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr


if __name__ == "__main__":
    print(User(
        username="Alex",
        hashed_password="qasdnvjanvijnaiesudfhnvajoidfvna134uy589q0wehr",
        email="bobkovalex.yaundex.ru@yandex.ru"
    ))
    print(User(
        username="Alex",
        hashed_password="qasdnvjanvijnaiesudfhnvajoidfvna134uy589q0wehr",
        email="Alex@zsv"
    ))
