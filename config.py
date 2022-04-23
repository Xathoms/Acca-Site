from models import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "mysql://xathoms:Xath3488@195.231.19.190:3306/ACCA?charset=utf8mb4"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo_pool=True,
    pool_size=10,
    max_overflow=20,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

session = Session(engine)

class Settings:
    PROJECT_NAME:str = "ACCA Site"
    PROJECT_VERSION: str = "1.0.0"

settings = Settings()