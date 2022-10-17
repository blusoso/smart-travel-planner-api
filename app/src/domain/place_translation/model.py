from sqlalchemy import Column, String,  DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ...database import Base


class PlaceTranslation(Base):
    __tablename__ = 'place_translations'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    name = Column(String)
    language_code_id = Column(String, ForeignKey('language_codes.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_translations')
    language_code = relationship(
        'LanguageCode', back_populates='place_translations'
    )
