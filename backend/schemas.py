from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str = None

class User(BaseModel):
    email: str = None
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str
