from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

#określenie adresy bazy danych
SQLALCHEMY_DATABASE_URL = "postgresql://user_1:postgres@localhost:5432/users"

#utworzenie silnik potrzebnego do komunikacji z bazą
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#utworzenie sesji lokalnej dzięki której możliwe jest wykonywanie operacji na bazie danych
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#okreslenie sekretnego klucza względem którego odbywa się dehashowania oraz algorytmu hashującego
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#przypisanie instancji CryptContext zawierającej motody umożliwaijące weryfikację hasła
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#przypisanie zmiennej umożliwiającej uwierzytelnienie przy pomocy tokena 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")