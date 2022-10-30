from sqlalchemy import Column, String, Unicode
from sqlalchemy.orm import relationship

from app.db.pgsql.base_declarative import Base


class User(Base):
    username = Column(String, nullable=False, unique=True)
    password = Column(Unicode(255), nullable=False)
    role = Column(String, nullable=False)
    patients = relationship("Patient")
