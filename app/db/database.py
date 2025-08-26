import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv 

load_dotenv()

# URL базы данных
DATABASE_URL = os.getenv("DATABASE_URL") 

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL) # pyright: ignore
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
