from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ....database import Base


class PlaceImg(Base):
    __tablename__ = 'place_imgs'

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, ForeignKey('places.id'))
    img_desktop = Column(String)
    img_mobile = Column(String, nullable=True)
    is_thumbnail = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    place = relationship('Place', back_populates='place_imgs')
