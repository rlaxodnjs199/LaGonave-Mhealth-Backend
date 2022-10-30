from fastapi import APIRouter, Depends

from .dal import PatientDAL, get_patient_dal
from .schemas import CreatePatientRequestSchema

router = APIRouter()


@router.post("/")
async def create_patient(
    new_patient: CreatePatientRequestSchema,
    patient_dal: PatientDAL = Depends(get_patient_dal),
):
    new_patient = await patient_dal.create_patient(new_patient)

    return new_patient


@router.get("/")
async def get_patient_full_name(
    patient_id: str,
    patient_dal: PatientDAL = Depends(get_patient_dal),
):
    patient = await patient_dal.get_patient_full_name(patient_id)

    return patient
