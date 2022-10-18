from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class PlaceFee(Base):
    __tablename__ = 'place_fees'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    child_fee = Column(Float, default=0.0, nullable=True)
    adult_fee = Column(Float, default=0.0, nullable=True)
    foreigner_child_fee = Column(Float, default=0.0, nullable=True)
    foreigner_adult_fee = Column(Float, default=0.0, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_fees')
