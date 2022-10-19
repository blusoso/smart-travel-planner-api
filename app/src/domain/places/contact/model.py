from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ....database import Base


class PlaceContact(Base):
    __tablename__ = 'place_contacts'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    phones = Column(ARRAY(String), nullable=True)
    emails = Column(ARRAY(String), nullable=True)
    urls = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_contacts')
