

from app.courses.course_model import CourseResponse, Course, CourseListResponse


class CourseService:
    def __init__(self, course_mediator = None) -> None:
        self.course_mediator = course_mediator


    def create_course(self, course: Course) -> CourseResponse:
        course_data = self.course_mediator.create(course)
        response: CourseResponse = CourseResponse(success=True, data=course_data)
        return response

    def list_course(self) -> CourseListResponse:
        courses = self.course_mediator.list()
        response: CourseListResponse = CourseListResponse(success=True, data=courses)
        return response