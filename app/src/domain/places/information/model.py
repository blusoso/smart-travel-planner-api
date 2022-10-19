from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ....database import Base


class PlaceInformation(Base):
    __tablename__ = 'place_information'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    intro = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    activities = Column(ARRAY(String), nullable=True)
    facilities = Column(ARRAY(String), nullable=True)
    how_to_travel = Column(Text, nullable=True)
    how_to_travel = Column(Text, nullable=True)
    language_code_id = Column(String, ForeignKey('language_codes.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_information')
    language_code = relationship(
        'LanguageCode', back_populates='place_information'
    )
