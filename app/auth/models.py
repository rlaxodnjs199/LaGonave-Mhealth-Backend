from sqlalchemy import Column, String

from app.db.pgsql.base_declarative import Base


class User(Base):
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
