from fastapi import APIRouter, Depends

from .dal import PatientDAL, get_patient_dal
from .schemas import CreatePatientRequestSchema, CreatePatientResponseSchema

router = APIRouter()


@router.post("/", response_model=CreatePatientResponseSchema)
async def create_patient(
    new_patient_record: CreatePatientRequestSchema,
    patient_dal: PatientDAL = Depends(get_patient_dal),
):
    new_patient = await patient_dal.create_patient(new_patient_record)

    return new_patient
