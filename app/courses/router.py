from fastapi import APIRouter

from app.courses.course_repository import CourseDynaRepository
from app.courses.course_service import CourseService
from app.courses.course_mediator import CourseMediator, ICourseMediator
from app.courses.course_model import Course


router1 = APIRouter()
repo_course = CourseDynaRepository()
course_service: CourseService = CourseService()
mediator: ICourseMediator= CourseMediator(course_service, repo_course)

@router1.get('/')
def get_courses():
    return 'List of courses'


@router1.get('/{id}')
def get_course(id: int):
    return f'Course {id}'


@router1.post('/')
def create_course(course: Course):
    response = mediator.create(course)
    return response

@router1.get('/list/all')
def get_courses_list():
    response = mediator.list()
    return response