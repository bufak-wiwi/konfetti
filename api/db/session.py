import os
from dotenv import load_dotenv

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_USER : str = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER : str = os.getenv("DB_SERVER")
DB_PORT : str = os.getenv("DB_PORT")
DB_DATABASE : str = os.getenv("DB_DATABASE")

DATABASE_URL = f"mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()