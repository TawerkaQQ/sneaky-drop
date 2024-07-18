import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine, MetaData
from models import Base
from config.db_config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

dsn = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(dsn, echo=True)

Base.metadata.create_all(engine)
