from fastapi import APIRouter
from ...config import PLACE_ROUTE_PREFIX_V1
from . import places, contacts, fees, imgs, information, locations, opening_periods, translations

router = APIRouter()


def include_places_api_routes():
    router.include_router(places.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(contacts.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(fees.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(imgs.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(information.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(locations.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(opening_periods.router, prefix=PLACE_ROUTE_PREFIX_V1)
    router.include_router(translations.router, prefix=PLACE_ROUTE_PREFIX_V1)


include_places_api_routes()
