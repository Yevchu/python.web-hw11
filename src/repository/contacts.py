from typing import List
from datetime import datetime, timedelta, date

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel

async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

async def get_contact_by_first_name(contact_first_name: str, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.first_name == contact_first_name).first()

async def get_contact_by_last_name(contact_last_name: str, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.last_name == contact_last_name).first()

async def get_contact_by_email(contact_email: str, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.email == contact_email).first()

async def upcoming_birthday(db: Session) -> List[Contact]:
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    return db.query(Contact).filter(Contact.birthday >= today, Contact.birthday <= end_date).all()

async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        birthday=body.birthday,
        description=body.description
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.birthday = body.birthday
        contact.description = body.description
        db.commit()
    return contact

async def delete_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact