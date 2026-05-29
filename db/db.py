import os
from dotenv import load_dotenv # <-- Accede a la info del archivo ".env"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL_LOCAL")
print(DATABASE_URL)
print(repr(DATABASE_URL))
try:
    print(list(DATABASE_URL.encode('utf-8')))
    print(len(DATABASE_URL))
except Exception as e:
    print('encode error:', e)

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind= engine
)

base = declarative_base() #<-- Almacena las declaraciones de la base de datos, la cual se traduce en las configuraciones de la misma.
print ("Connected to DB= OK")