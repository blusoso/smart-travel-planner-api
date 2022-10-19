from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ....database import Base


class PlaceOpeningPeriod(Base):
    __tablename__ = 'place_opening_periods'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    day_id = Column(Integer, ForeignKey('days.id'))
    open_id = Column(Integer, ForeignKey('time_periods.id'))
    close_id = Column(Integer, ForeignKey('time_periods.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_opening_periods')
    day = relationship('Day', back_populates='place_opening_periods')
    open = relationship('TimePeriods', foreign_keys=[open_id])
    close = relationship('TimePeriods', foreign_keys=[close_id])
