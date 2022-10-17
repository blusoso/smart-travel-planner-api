import enum
from sqlalchemy import Column, String, Float, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ...database import Base


class CATEGORY_TYPE(enum.Enum):
    ATTRACTION = 'attraction'
    RESTAURANT = 'restaurant'
    SHOP = 'shop'


class Place(Base):
    __tablename__ = 'places'

    id = Column(String, primary_key=True, index=True)
    latitude = Column(Float, default=0.0)
    longitude = Column(Float, default=0.0)
    tags = Column(ARRAY(String), nullable=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    country = relationship('Country', back_populates='places')
    place_translations = relationship(
        'PlaceTranslation', back_populates='place'
    )
    place_locations = relationship('PlaceLocation', back_populates='places')
