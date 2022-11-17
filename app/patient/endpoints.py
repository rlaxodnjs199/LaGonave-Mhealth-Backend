from typing import List, Dict
from uuid import UUID

from fastapi import APIRouter, Depends, Query
from pydantic import Required

from .dal import PatientDAL, get_patient_dal
from .schemas import (
    CreatePatientRequestSchema,
    CreatePatientResponseSchema,
    GetPatientResponseSchema,
    GetPatientDemographicSchema,
)

router = APIRouter()


@router.post("/", response_model=CreatePatientResponseSchema)
async def create_patient(
    new_patient_record: CreatePatientRequestSchema,
    patient_dal: PatientDAL = Depends(get_patient_dal),
):
    new_patient = await patient_dal.create_patient(new_patient_record)

    return new_patient


@router.get("/", response_model=List[GetPatientResponseSchema])
async def get_patients_by_phone_number(
    phone_number: str = Query(
        default=Required, min_length=10, max_length=10, regex="^[0-9]+$"
    ),
    patient_dal: PatientDAL = Depends(get_patient_dal),
):
    patients = await patient_dal.get_patients_by_phone_number(phone_number)

    return patients


@router.get("/{patient_id}/demographics", response_model=GetPatientDemographicSchema)
async def get_patient_demographics(
    patient_id: UUID, patient_dal: PatientDAL = Depends(get_patient_dal)
):
    patient = await patient_dal.get_patient(patient_id)

    return patient


@router.get("/{patient_id}/checkups")
async def get_patient_checkups(
    patient_id: UUID, patient_dal: PatientDAL = Depends(get_patient_dal)
):
    checkups = await patient_dal.get_patient_checkups(patient_id)

    return checkups


@router.post("/{patient_id}/checkups")
async def create_patient_checkup(
    patient_id: UUID,
    checkup_data: Dict,
    patient_dal: PatientDAL = Depends(get_patient_dal),
):
    await patient_dal.create_patient_checkup(patient_id, checkup_data)


@router.get("/{patient_id}/checkups/{checkup_id}")
async def get_patient_checkup():
    pass
