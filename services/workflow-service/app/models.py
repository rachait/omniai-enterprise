from sqlalchemy import Column, Integer, String, JSON
from .database import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        nullable=False
    )

    definition = Column(
        JSON,
        nullable=False
    )
