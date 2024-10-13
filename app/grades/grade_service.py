from abc import ABC, abstractmethod

from app import constants
from app.constants import Constants
from app.grades.grade_repository import GradeDynaRepository
from app.grades.grades_model import GradeListResponse, GradeKey


class IGradeService(ABC):
    @abstractmethod
    def get_grades_by_courses(self, course_id:str, grade_id: str) -> GradeListResponse:
        pass

class GradeService(IGradeService):
    def __init__(self, repo = GradeDynaRepository) -> None:
        self.repo = repo

    def get_grades_by_courses(self, course_id:str, grade_id: str) -> GradeListResponse:
        grade_key: GradeKey = GradeKey()
        grade_key.add_prefix(course_id, grade_id)
        grades = self.repo.list_by_key(pk_key=Constants.SK_KEY, pk_data=grade_key.course, sk_key=Constants.GRADE_KEY, sk_data=grade_key.grade)
        response: GradeListResponse = GradeListResponse(success=True, grades=grades)
        return response

