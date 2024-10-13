from fastapi import APIRouter

from app.grades.grade_repository import GradeDynaRepository
from app.grades.grade_service import GradeService, IGradeService
from app.grades.grades_model import GradeSchema, GradeListResponse

router = APIRouter()


repo: GradeDynaRepository = GradeDynaRepository()
grade_service: IGradeService = GradeService(repo)


@router.get('/{course_id}/{grade_id}')
def get_grades(course_id: str, grade_id: str) -> GradeListResponse:
    grades = grade_service.get_grades_by_courses(course_id, grade_id)
    return grades