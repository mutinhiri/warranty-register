from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Warranty(Base):
    __tablename__ = "warranties"
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String, index=True)
    asset_serial = Column(String)
    registered_by = Column(String)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())
