import logging
from typing import List

from faker import Faker
from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from data_generator.schema import PersonSchema, FullProfileSchema
from data_generator.utils import Properties, Person, FullProfile

logger = logging.getLogger(__name__)

route = APIRouter()

store = {}


@route.on_event("startup")
def startup_event():
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
        data = [Person.generate(fake=store["fake"]) for _ in range(n)]
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
        print(data)
        return data
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to process request"
        )
