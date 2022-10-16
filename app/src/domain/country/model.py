from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, index=True)
    name_th = Column(String)
    name_en = Column(String)
    language_code = Column(String(3))
    flag_img = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    places = relationship('Place', back_populates='country')
