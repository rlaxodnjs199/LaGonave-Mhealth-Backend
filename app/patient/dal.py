from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.pgsql.session import get_db
from .models import Patient
from .schemas import CreatePatientRequestSchema


class PatientDAL:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_patient(self, new_patient: CreatePatientRequestSchema):
        new_patient = Patient(**new_patient.dict())
        print(new_patient)
        self.db_session.add(new_patient)
        await self.db_session.commit()

        return new_patient

    async def get_patient_full_name(self, patient_id: str):
        q = await self.db_session.execute(
            select(Patient).where(Patient.id == patient_id)
        )

        return q.scalars().first().age


def get_patient_dal(db=Depends(get_db)) -> PatientDAL:
    return PatientDAL(db)
