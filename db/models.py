from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class MailAccount(Base):
    __tablename__ = 'mail_account'

    phone_number = Column(String, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    birthday = Column(Date, nullable=True)
    sex = Column(String, nullable=True)
    email = Column(String, nullable=False)
