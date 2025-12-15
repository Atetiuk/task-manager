from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

while True:
    try:
        conn = psycopg2.connect(
            dbname="task_manager",
            user="postgres",
            password="password",
            host="db",
            port="5432"
        )
        conn.close()
        break
    except:
        time.sleep(1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
