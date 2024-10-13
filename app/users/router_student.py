from fastapi import APIRouter

from app.users.student_model import Student, StudentResponse, StudentListResponse
from app.users.student_service import StudentService

router = APIRouter()

student_service: StudentService = StudentService()

@router.get("/")
def get_students() -> StudentListResponse:
    """
    prueba de doc
    :return:
    """
    response = student_service.list_users()

    return response

@router.post("/")
def create_student(student: Student) -> StudentResponse:
    response = student_service.create_user(student)
    return response
