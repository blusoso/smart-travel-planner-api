from fastapi import APIRouter

from ..config import ROUTE_PREFIX_V1
from . import users, places, countries, language_codes, place_translations, attraction_types, place_locations, place_contacts, place_fees, place_information, time_periods, days, place_opening_periods, place_imgs
from .places.api import router as places_router_api

router = APIRouter()


def include_api_routes():
    router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(places_router_api, prefix=ROUTE_PREFIX_V1)
    router.include_router(countries.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(language_codes.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(time_periods.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(days.router, prefix=ROUTE_PREFIX_V1)


include_api_routes()
