from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database import Base


class AttractionType(Base):
    __tablename__ = 'attraction_types'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tourism_type_id = Column(Integer, ForeignKey(
        'tourism_types.id'), nullable=True)
    language_code_id = Column(String(3), ForeignKey(
        'language_codes.id'), nullable=True
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    tourism_type = relationship(
        'TourismType', back_populates='attraction_types'
    )
    language_code = relationship(
        'LanguageCode', back_populates='attraction_types'
    )
