# from typing import List
# from datetime import datetime, timedelta

# from fastapi import Depends
# from sqlalchemy.orm import sessionmaker, Session, declarative_base
# from sqlalchemy import Column, String, Integer, func, Date, create_engine
# from sqlalchemy.sql.sqltypes import DateTime


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:567234@localhost:5432/rest_app"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# class Contact(Base):
#     __tablename__ = 'contacts'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     first_name = Column(String(25), nullable=False)
#     last_name = Column(String(25), nullable=False)
#     email = Column(String(120), nullable=False, unique=True)
#     birthday = Column(Date, nullable= False)
#     description = Column(String, nullable=True)
#     created_at = Column('created_at', DateTime, default=func.now())

# def upcoming_birthday(db: Session) -> List[Contact]:
#     today = datetime.today().date()
#     end_date = today + timedelta(days=7)
#     return db.query(Contact).filter(Contact.birthday >= today, Contact.birthday <= end_date).all()

# def get_contact_by_email(contact_email: str, db: Session) -> Contact:
#     return db.query(Contact).filter(Contact.email == contact_email).first()


# print(upcoming_birthday(db = SessionLocal()))