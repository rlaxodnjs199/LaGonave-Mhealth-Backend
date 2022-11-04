from fastapi import Depends
from sqlalchemy import select
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

        return new_patient

    async def get_patients_by_phone_number(self, phone_number: str):
        q = await self.db_session.execute(
            select(Patient).where(Patient.phone_number == phone_number)
        )
        patients = q.scalars().all()
        await self.db_session.commit()

        return patients


def get_patient_dal(db=Depends(get_db)) -> PatientDAL:
    return PatientDAL(db)
