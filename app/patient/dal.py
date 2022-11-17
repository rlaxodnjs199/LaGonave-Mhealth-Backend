from uuid import UUID
from typing import Dict

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.pgsql.session import get_db
from .models import Patient
from .schemas import CreatePatientRequestSchema
from app.checkup.models import Checkup


class PatientDAL:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_patient(self, new_patient_record: CreatePatientRequestSchema):
        new_patient = Patient(**new_patient_record.dict())
        self.db_session.add(new_patient)
        await self.db_session.commit()

        return new_patient

    async def get_patient(self, patient_id: UUID):
        q = await self.db_session.execute(
            select(Patient).where(Patient.id == patient_id)
        )
        patient = q.scalars().first()
        await self.db_session.commit()

        return patient

    async def get_patients_by_phone_number(self, phone_number: str):
        q = await self.db_session.execute(
            select(Patient).where(Patient.phone_number == phone_number)
        )
        patients = q.scalars().all()
        await self.db_session.commit()

        return patients

    async def get_patient_checkups(self, patient_id: UUID):
        q = await self.db_session.execute(
            select(Patient)
            .where(Patient.id == patient_id)
            .options(selectinload(Patient.checkups))
        )
        patient = q.scalars().first()
        checkups = patient.checkups
        await self.db_session.commit()

        return checkups

    async def create_patient_checkup(self, patient_id: UUID, checkup_data: Dict):
        q = await self.db_session.execute(
            select(Patient)
            .where(Patient.id == patient_id)
            .options(selectinload(Patient.checkups))
        )
        patient = q.scalars().first()
        new_checkup = Checkup(data=checkup_data)
        patient.checkups.append(new_checkup)
        self.db_session.add(patient)
        await self.db_session.commit()


def get_patient_dal(db=Depends(get_db)) -> PatientDAL:
    return PatientDAL(db)
