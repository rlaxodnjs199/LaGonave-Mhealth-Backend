from sqlalchemy import Column, String

from app.db.pgsql.base_declarative import Base


class User(Base):
    __tablename__ = "user"

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
