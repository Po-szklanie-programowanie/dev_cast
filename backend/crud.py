from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta
from typing import Optional
import models
import schemas
import database

# sprawdzenie zgodności wpisywanego hasła z zahashowanym hasłem
def verify_password(plain_password: str, hashed_password: str):
    return database.pwd_context.verify(plain_password, hashed_password)

# zwrócenie oryginalnego hasła wprowadzanego przez użytkownika w zahashowanej postaci
def get_password_hash(password):
    return database.pwd_context.hash(password)

# pobieranie danych użytkownika z bazy
def get_user(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# utworzenie nowego użytkownika zgodnie z danymi z obiektu user przy jednoczesnym hashowaniu hasła
def create_user(db: Session, user: schemas.UserInDB):
    db_user = models.User(email=user.email, hashed_password=get_password_hash(user.hashed_password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# pobranie danych użytkownika i sprawdzenie zgodności wpisywanych haseł
def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# generowanie tokenu dostępu
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, database.SECRET_KEY, algorithm=database.ALGORITHM)
    return encoded_jwt
