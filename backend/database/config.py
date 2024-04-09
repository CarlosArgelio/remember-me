from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

Base = declarative_base()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()