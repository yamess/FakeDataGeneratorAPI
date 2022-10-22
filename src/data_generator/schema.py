from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr


class PersonSchema(BaseModel):
    first_name: str
    last_name: str
    language_name: str
    prefix: str

    class Config:
        orm_mode = True


class FullProfileSchema(BaseModel):
    username: str
    name: str
    sex: str
    address: str
    mail: EmailStr
    birthdate: date
    job: str
    company: str
    ssn: str
    residence: str
    current_location: list
    blood_group: str
    website: List[str]
