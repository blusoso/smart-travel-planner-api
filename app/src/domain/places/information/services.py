from sqlalchemy.orm import Session
from pythainlp.corpus import thai_stopwords
from pythainlp.tokenize import word_tokenize
from typing import List
import re

from . import model, schema
from ..place.model import Place
from ..translation.model import PlaceTranslation
from ..location.model import PlaceLocation
from ..contact.model import PlaceContact
from ..fee.model import PlaceFee
from ..img.model import PlaceImg
from ...country.model import Country

DEFAULT_LIMIT_PLACE_INFO = 100
STOP_WORDS = list(thai_stopwords())


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


def attraction_type_text(attraction_type_arr):
    text = ''
    if attraction_type_arr is not None:
        for attraction_type in attraction_type_arr:
            text += str(attraction_type + ' ')
    return text


def combined_text(name, attraction_type_list, intro, desc):
    return name + ' ' + attraction_type_text(attraction_type_list) + ' ' + intro + ' ' + desc


def clean_th_text(text):
    text = str(text)
    text = re.sub('[^ก-๙]', '', text)
    sentence = word_tokenize(text)
    result = [
        word for word in sentence if word not in STOP_WORDS and " " not in word]
    # result = convert_arr_to_arr_str(result)
    return result


def create_place_information(
        place_information: schema.PlaceInformationCreate,
        name: str,
        attraction_type_list: List[str],
        db: Session
):
    long_text = combined_text(name, attraction_type_list,
                              place_information.intro, place_information.description)
    bag_of_words = clean_th_text(long_text)

    db_place_information = model.PlaceInformation(
        place_id=place_information.place_id,
        intro=place_information.intro,
        description=place_information.description,
        activities=place_information.activities,
        facilities=place_information.facilities,
        how_to_travel=place_information.how_to_travel,
        bag_of_words=bag_of_words,
        language_code_id=place_information.language_code_id,
    )
    db.add(db_place_information)
    db.commit()
    db.refresh(db_place_information)
    return db_place_information
