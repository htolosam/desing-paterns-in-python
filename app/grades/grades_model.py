from pydantic import BaseModel

from app.constants import Constants


class GradeSchema(BaseModel):
    pk: str
    sk: str
    grade: str
    comment: str = None
    note1: int
    note2: int
    note3: int


class Grade(BaseModel):
    student_id: str
    class_id: str
    grade: str
    comment: str
    note1: int
    note2: int
    note3: int

class GradeListResponse(BaseModel):
    success: bool = False
    grades: list[Grade]

class GradeKey(BaseModel):
    course: str = ""
    grade: str = ""
    def add_prefix(self, pk_data: str, sk_data:str) ->None:
        self.course = f"{Constants.COURSE_PREFIX}{pk_data}"
        self.grade = f"{Constants.GRADE_PREFIX}{sk_data}"