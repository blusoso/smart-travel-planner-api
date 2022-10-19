from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

API_PREFIX = "/api"
ROUTE_PREFIX_V1 = "/v1"
PLACE_ROUTE_PREFIX_V1 = '/places'

config = Config(".env")

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
