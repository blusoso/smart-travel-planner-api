from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy import func

from ..places.place.model import Place
from ..places.translation.model import PlaceTranslation
from ..places.location.model import PlaceLocation
from ..country.model import Country

DEFAULT_LIMIT_PLACE = 100


def search_places_by_keyword(db: Session, keyword: str, skip: int = 0, limit: int = DEFAULT_LIMIT_PLACE):
    keyword = keyword.casefold()

    search_results = db.query(
        Place,
        PlaceTranslation.name,
        Country.name.label('country_name'),
        PlaceLocation
    )\
        .join(PlaceTranslation)\
        .join(Country)\
        .join(PlaceLocation)\
        .filter(func.lower(PlaceTranslation.name).contains(keyword))\
        .offset(skip)\
        .limit(limit)\
        .all()

    return search_results
