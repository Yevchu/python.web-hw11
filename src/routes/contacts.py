from typing import List
from datetime import date

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactModel, ResponseModel
from src.repository import contacts as repository_contact

from pydantic import EmailStr

router = APIRouter(prefix='/contacts', tags=['contacts'])

@router.get('/', response_model=List[ResponseModel])
async def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contacts = await repository_contact.get_contacts(skip, limit, db)
    return contacts

@router.get('/firts_name/{first_name}', response_model=ResponseModel)
async def get_contact_by_first_name(first_name: str, db: Session = Depends(get_db)):
    contact = await repository_contact.get_contact_by_first_name(first_name, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=('Contact not found'))
    return contact

@router.get('/last_name/{last_name}', response_model=ResponseModel)
async def get_contact_by_last_name(last_name: str, db: Session = Depends(get_db)):
    contact = await repository_contact.get_contact_by_last_name(last_name, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=('Contact not found'))
    return contact

@router.get('/email/{email}', response_model=ResponseModel)
async def get_contact_by_email_name(email: EmailStr, db: Session = Depends(get_db)):
    contact = await repository_contact.get_contact_by_email(email, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=('Contact not found'))
    return contact

@router.get('/upcoming_birthay', response_model=List[ResponseModel])
async def upcoming_birthday(db: Session = Depends(get_db)):
    contact = await repository_contact.upcoming_birthday(db)
    if contact is []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=('No contacts in this time area'))
    return contact


@router.post('/', response_model=ResponseModel)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    return await repository_contact.create_contact(body, db)

@router.put('/{contact_id}', response_model=ResponseModel)
async def change_contact(contact_id: int, body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contact.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not fund')
    return contact

@router.delete('/{contact_id}', response_model=ResponseModel)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contact.delete_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found')
    return contact