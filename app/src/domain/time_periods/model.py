from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class TimePeriods(Base):
    __tablename__ = 'time_periods'

    id = Column(Integer, primary_key=True, index=True)
    time = Column(String(4))
