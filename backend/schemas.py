from pydantic import BaseModel

# klasa przechowująca tok czyli unikalny ciąg znaków generowany dla zalogowanego użytkownika
class Token(BaseModel):
    access_token: str
    token_type: str

# pole przechowuje adres e-mail użytkownika przypisanego do tokenu
class TokenData(BaseModel):
    email: str = None

# klasa przechowująca e-mail używany do weryfikacji logowanego oraz dodawanego użytkownika
class User(BaseModel):
    email: str = None
    class Config:
        orm_mode = True

# zahaszowane hasło przypisane do konkretnego użytkownika
class UserInDB(User):
    hashed_password: str
