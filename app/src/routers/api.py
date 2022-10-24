from fastapi import APIRouter


from ..config import ROUTE_PREFIX_V1
from . import users, countries, language_codes, time_periods, days, attraction_types, search, tourism_type
from .places.api import router as places_router_api

router = APIRouter()


def include_api_routes():
    router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(places_router_api, prefix=ROUTE_PREFIX_V1)
    router.include_router(countries.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(attraction_types.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(tourism_type.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(language_codes.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(time_periods.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(days.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(search.router, prefix=ROUTE_PREFIX_V1)


include_api_routes()
