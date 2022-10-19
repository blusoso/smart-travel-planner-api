from sqlalchemy import Column, String, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ...database import Base


class LanguageCode(Base):
    __tablename__ = 'language_codes'

    id = Column(String(3), primary_key=True, index=True)
    language_en = Column(String)
    language_native = Column(String)

    country = relationship('Country', back_populates='language_code')
    place_translations = relationship(
        'PlaceTranslation', back_populates='language_code'
    )
    attraction_types = relationship(
        'AttractionType', back_populates='language_code'
    )
    place_locations = relationship(
        'PlaceLocation', back_populates='language_code'
    )
    place_information = relationship(
        'PlaceInformation', back_populates='language_code'
    )
