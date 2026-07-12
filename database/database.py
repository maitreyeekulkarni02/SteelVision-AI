"""
SteelVision AI
Database Configuration

Stores industrial inspection history.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database for MVP
DATABASE_URL = "sqlite:///steelvision_history.db"


# Database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# Database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base model class
Base = declarative_base()



def get_database():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()