import logging
from typing import List

from faker import Faker
from faker_airtravel import AirTravelProvider
from faker_education import SchoolProvider
from faker_vehicle import VehicleProvider
from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from data_generator.schema import PersonSchema, FullProfileSchema, SimpleProfileSchema, AddressSchema, BankSchema, \
    AirportSchema, SchoolsSchema, VehiculeSchema, GeoPointSchema
from data_generator.utils import Properties, Person, FullProfile, SimpleProfile, Address, Bank, Airport, Schools, \
    Vehicule, GeoPoint

logger = logging.getLogger(__name__)

route = APIRouter()

store = {}


@route.on_event("startup")
def startup_event():
    logger.info("Startup event")
    fake = Faker()
    fake.add_provider(AirTravelProvider)
    store["fake"] = Faker()


@route.head("/data")
async def head_properties():
    try:
        prop = [member.value for member in Properties]
        headers = {"content-length": str(len(prop)), "allowed-values": str(prop)}
        return JSONResponse(content=None, headers=headers)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/person", response_model=List[PersonSchema])
async def ger_person(n: int = 1):
    try:
        fake = store["fake"]
        data = [Person.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/full-profile", response_model=List[FullProfileSchema])
async def get_full_profile(n: int = 1):
    try:
        fake = store["fake"]
        data = [FullProfile.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/simple-profile", response_model=List[SimpleProfileSchema])
async def get_simple_profile(n: int = 1):
    try:
        fake = store["fake"]
        data = [SimpleProfile.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/address", response_model=List[AddressSchema])
async def get_address(n: int = 1):
    try:
        fake = store["fake"]
        data = [Address.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get('/data/bank', response_model=List[BankSchema])
def get_bank(n: int = 1):
    try:
        fake = store["fake"]
        data = [Bank.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/airport", response_model=List[AirportSchema])
async def get_airport(n: int = 1):
    try:
        fake = Faker()
        fake.add_provider(AirTravelProvider)
        data = [Airport.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(f"ERROR: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/school", response_model=List[SchoolsSchema])
async def get_school(n: int = 1):
    try:
        fake = Faker()
        fake.add_provider(SchoolProvider)
        data = [Schools.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/vehicule", response_model=List[VehiculeSchema])
async def get_vehicule(n: int = 1):
    try:
        fake = Faker()
        fake.add_provider(VehicleProvider)
        data = [Vehicule.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )


@route.get("/data/geo-points", response_model=List[GeoPointSchema])
async def get_geo_points(n: int = 1):
    try:
        fake = store["fake"]
        data = [GeoPoint.generate(fake=fake) for _ in range(n)]
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )
