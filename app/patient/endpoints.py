from typing import List

from fastapi import APIRouter, Depends, Query
from pydantic import Required

from .dal import PatientDAL, get_patient_dal
from .schemas import (
    CreatePatientRequestSchema,
    CreatePatientResponseSchema,
    GetPatientResponseSchema,
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
