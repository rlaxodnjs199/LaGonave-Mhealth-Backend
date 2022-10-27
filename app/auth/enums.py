from enum import Enum


class RoleEnum(str, Enum):
    admin = "admin"
    doctor = "doctor"
    staff = "staff"
    patient = "patient"
