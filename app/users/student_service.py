from app.users.student_dynamo_repository import StudentDynaRepository
from app.users.student_model import Student, StudentResponse, StudentListResponse


class StudentService:

    def __init__(self)->None:
        self.student_repo: StudentDynaRepository = StudentDynaRepository()

    def create_user(self, student: Student) -> StudentResponse:
        student = self.student_repo.create_student(student)
        student_response: StudentResponse = StudentResponse(success=True, data=student)
        return student_response


    def list_users(self) -> StudentListResponse:
        list_student = self.student_repo.list_students()
        student_response: StudentListResponse = StudentListResponse(success=True, data=list_student)
        return student_response