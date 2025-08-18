from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from infrastructure.database import Base
from domain.models.enums import TaskType
import uuid

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    type = Column(String, default="Task", nullable=False)
