from fastapi import APIRouter

from ..config import ROUTE_PREFIX_V1
from . import users, places, countries, language_codes, place_translations, attraction_types, place_locations, place_contacts, place_fees, place_information, time_periods, days, place_opening_periods, place_imgs

router = APIRouter()


def include_api_routes():
    router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(places.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(countries.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(language_codes.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_translations.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(attraction_types.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_locations.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_contacts.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_fees.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_information.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(time_periods.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(days.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_opening_periods.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(place_imgs.router, prefix=ROUTE_PREFIX_V1)


include_api_routes()
