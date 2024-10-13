from fastapi import FastAPI

from app.users.router_student import router as student_router
from app.courses.router import router1 as course_router
from app.grades.router import router as grades_router
from app.report.router import router as file_router


app = FastAPI()

app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(course_router, prefix="/courses", tags=["courses"])
app.include_router(grades_router, prefix="/grades", tags=["grades"])
#
app.include_router(file_router, prefix="/report", tags=["report"])


@app.get("/")
def health_check():
    return {"status": "ok"}