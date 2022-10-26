from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class TourismType(Base):
    __tablename__ = 'tourism_types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    language_code_id = Column(String(3), ForeignKey('language_codes.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    attraction_types = relationship(
        'AttractionType', back_populates='tourism_type'
    )
    language_code = relationship(
        'LanguageCode', back_populates='tourism_types'
    )
