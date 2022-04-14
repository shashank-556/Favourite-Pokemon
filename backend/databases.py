from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import ujson

with open('secrets.json','r') as fh :
    js = ujson.load(fh)
    user = js["DB_USER"]
    password = js["DB_PASSWORD"]

database_url = f'mysql://{user}:{password}@localhost:3306/edvora'
engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

