from sqlalchemy import Column, Integer, String
from .database import Base


class Execution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, index=True)

    workflow_id = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )
