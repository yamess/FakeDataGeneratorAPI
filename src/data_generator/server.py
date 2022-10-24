import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from data_generator import routes
from data_generator.const import VERSION

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Rest API for fake data generation",
    version=VERSION,
    docs_url="/docs"
)

app.include_router(router=routes.route, prefix=("/" + VERSION), tags=["PersonData"])

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], expose_headers=["*"]
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
