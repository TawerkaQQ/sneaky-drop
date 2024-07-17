import os

from sqlalchemy import create_engine

db_name = 'sneaky-drop'
db_path = os.path.join(os.getcwd(), db_name)

engine = create_engine(f'sqlite:///{db_path}', echo=True)
