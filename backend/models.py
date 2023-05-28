from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqlalchemy

#utworzenie klasy bazowej ułatwiającej definicję klasy User
base = sqlalchemy.orm.declarative_base()

#utworzenie modelu danych dla tabeli wykorzystywanej przez bazę danych
class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)