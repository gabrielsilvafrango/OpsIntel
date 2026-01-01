import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    name = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    role = Column(String(50), nullable=False, default="user")
    position = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)