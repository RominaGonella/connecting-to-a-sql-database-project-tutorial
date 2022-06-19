### SI ANTERIORMENTE YA EJECUTÉ APP.PY, EJECUTO ESTE ARCHIVO ANTES DE VOLVER A EJECUTAR APP.PY, ASI SE BORRAN LAS TABLAS Y LOS REGISTROS

import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = os.getenv("DB_CONNECTION")
# print(connection_string)
engine = create_engine(connection_string)
engine.connect()

#  borro las tablas
engine.execute("DROP TABLE book_authors;")
engine.execute("DROP TABLE books;")
engine.execute("DROP TABLE publishers;")
engine.execute("DROP TABLE authors;")
