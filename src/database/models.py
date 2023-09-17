from sqlalchemy import Column, String, Integer, func, Date
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    birthday = Column(Date, nullable= False)
    description = Column(String, nullable=True)
    created_at = Column('created_at', DateTime, default=func.now())