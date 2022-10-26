from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ....database import Base


class PlaceAttractionType(Base):
    __tablename__ = 'place_attraction_types'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    attraction_type_id = Column(Integer, ForeignKey('attraction_types.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship(
        'Place', back_populates='place_attraction_types'
    )
    attraction_type = relationship(
        'AttractionType', back_populates='place_attraction_types'
    )
