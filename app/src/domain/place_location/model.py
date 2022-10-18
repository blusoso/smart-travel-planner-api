from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class PlaceLocation(Base):
    __tablename__ = 'place_locations'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    address = Column(String, nullable=True)
    sub_district = Column(String)
    district = Column(String)
    province = Column(String)
    postcode = Column(String, nullable=True)
    geography = Column(String, nullable=True)
    language_code_id = Column(String, ForeignKey('language_codes.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_locations')
    language_code = relationship(
        'LanguageCode', back_populates='place_locations'
    )
