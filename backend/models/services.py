import uuid
from sqlalchemy import Column, String, DateTime, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Services(Base):
    __tablename__ = "services"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    name = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False, default="healthy")
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    avg_latency = Column(Integer, nullable=False)
    uptime_percentage = Column(Float, nullable=False)