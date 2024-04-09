from database.config import Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy import Column

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
