import enum
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from ...database import Base


class CATEGORY_TYPE(enum.Enum):
    ATTRACTION = 'attraction'
    RESTAURANT = 'restaurant'
    SHOP = 'shop'


class Place(Base):
    __tablename__ = 'places'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float, default=0.0)
    longitude = Column(Float, default=0.0)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
