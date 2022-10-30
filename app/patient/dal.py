from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.pgsql.session import get_db
from .models import Patient
from .schemas import CreatePatientRequestSchema


class PatientDAL:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_patient(self, new_patient_record: CreatePatientRequestSchema):
        new_patient = Patient(**new_patient_record.dict())
        self.db_session.add(new_patient)
        await self.db_session.commit()

        return new_patient.full_name


def get_patient_dal(db=Depends(get_db)) -> PatientDAL:
    return PatientDAL(db)
