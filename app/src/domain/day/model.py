from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class Day(Base):
    __tablename__ = 'days'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(3))

    place_opening_periods = relationship(
        'PlaceOpeningPeriod', back_populates='day')
