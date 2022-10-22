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


class SimpleProfileSchema(BaseModel):
    username: str
    name: str
    sex: str
    address: str
    mail: EmailStr
    birthdate: date


class AddressSchema(BaseModel):
    address: str
    building_number: str
    city: str
    country: str
    country_code: str
    postcode: str
    street_address: str
    street_name: str


class BankSchema(BaseModel):
    aba: str
    bank_country: str
    bban: str
    iban: str
    swift: str
    swift8: str
    swift11: str


class AirportSchema(BaseModel):
    airport: dict
    airline: str
    flight: dict


class SchoolsSchema(BaseModel):
    school: str
    district: str
    level: str
    type: str
    state: str
    nces_id: str


class VehiculeSchema(BaseModel):
    vehicule: dict
    machine: dict


class GeoPointSchema(BaseModel):
    longitude: float
    latitude: float
    lat_long: list
    local_lat_long: list
    location_on_land: list
