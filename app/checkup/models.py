from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID

from app.db.pgsql.base_declarative import Base


class Checkup(Base):
    data = Column(JSONB)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("lg_patient.id"), nullable=False)
