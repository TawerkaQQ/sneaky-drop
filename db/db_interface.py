import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine, Table, delete
from sqlalchemy.orm import sessionmaker
from config.db_config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
from models import MailAccount


class DBInterface:
    def __init__(self):
        self.engine = self.create_connection()
        self.Session = self.create_session()

    def create_connection(self):
        dsn = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(dsn)
        return engine

    def create_session(self):
        session = sessionmaker(bind=self.engine)
        return session

    def get_session(self):
        return self.Session()

    def get_object_from_table(self, table_name):
        '''
        возможно это лишнее
        '''
        table = Table(table_name, autoload_with=self.engine)
        return table

    def insert_into_mail_account(self, **arguments):
        with self.get_session() as session:
            account_to_add = MailAccount(phone_number=arguments['phone_number'],
                                         name=arguments['name'],
                                         surname=arguments['surname'],
                                         birthday=arguments['birthday'],
                                         sex=arguments['sex'],
                                         email=arguments['email'])
            session.add(account_to_add)
            session.commit()
        return self

    def delete_from_mail_account_by_phone(self, phone_number):
        with self.get_session() as session:
            stmt = delete(MailAccount).where(MailAccount.phone_number == phone_number)
            session.execute(stmt)
            session.commit()
        return self
