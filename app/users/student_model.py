from pydantic import BaseModel


class Student(BaseModel):
    pk: str
    sk: str
    name: str
    email: str

class StudentSchema(BaseModel):
    identification: str
    name: str
    email: str


class StudentListResponse(BaseModel):
    success: bool
    data: list[Student]

class StudentResponse(BaseModel):
    success: bool
    data: Student