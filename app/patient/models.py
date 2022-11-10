from datetime import date

from sqlalchemy import Column, ForeignKey, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property

from app.db.pgsql.base_declarative import Base


class Patient(Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Float)
    weight = Column(Float)
    phone_number = Column(String, nullable=False)
    address = Column(String)
    facility = Column(String)
    recorder_id = Column(UUID(as_uuid=True), ForeignKey("lg_user.id"), nullable=False)
    photo_url = Column(String)

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @hybrid_property
    def age(self):
        today = date.today()
        age = (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )

        return age
