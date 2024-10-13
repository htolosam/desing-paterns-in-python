import uuid

from pydantic import BaseModel


class CourseSchema(BaseModel):
    pk: str
    sk: str
    name: str
    def add_prefix(self, id: str) ->None:
        self.pk = "INSTITUTE#1"
        self.sk = f"COURSE#{id}"

class Course(BaseModel):
    id: str
    name: str

class CourseListResponse(BaseModel):
    success: bool
    data: list[Course]

class CourseResponse(BaseModel):
    success: bool
    data: Course
