from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from ..model import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student
)
from ..model import (
    StudentSchema,
    UpdateStudentModel,
    response_model,
    error_response_model
)


router = APIRouter()

@router.get("/students", response_description="Students retrieved")
async def get_students():
    student = await retrieve_students()
    if student:
        return response_model(student, "Students data retrieved successfully")
    return response_model(student, "Empty list returned")