from sqlalchemy.orm import Session
from . import model
from ..place.model import Place
from ..translation.model import PlaceTranslation
from ..location.model import PlaceLocation
from ..contact.model import PlaceContact
from ..fee.model import PlaceFee
from ..img.model import PlaceImg
from ...country.model import Country

DEFAULT_LIMIT_PLACE_INFO = 100


def get_place_information(
    db: Session,
    skip: int = 0,
    limit: int = DEFAULT_LIMIT_PLACE_INFO
):
    return db.query(model.PlaceInformation).offset(skip).limit(limit).all()


def get_place_information_detail(
    db: Session,
    lang_code: str,
    place_id: str
):
    place_information = db.query(
        PlaceImg,
        Place,
        PlaceTranslation,
        model.PlaceInformation,
        PlaceLocation,
        PlaceContact,
        PlaceFee
    )\
        .join(model.PlaceInformation)\
        .join(PlaceImg)\
        .join(PlaceTranslation)\
        .join(PlaceLocation)\
        .join(PlaceContact)\
        .join(PlaceFee)\
        .join(Country)\
        .filter(Place.id == place_id)\
        .filter(Place.is_active == True)\
        .filter(PlaceTranslation.language_code_id == lang_code)\
        .filter(Country.language_code_id == lang_code)\
        .first()

    return place_information
