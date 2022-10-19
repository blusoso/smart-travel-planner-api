from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    language_code_id = Column(String(3), ForeignKey('language_codes.id'))
    flag_img = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    places = relationship('Place', back_populates='country')
    language_code = relationship('LanguageCode', back_populates='country')
