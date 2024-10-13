from abc import ABC, abstractmethod

from app.courses.course_model import CourseSchema, Course
from app.courses.utils import get_course_to_schema, get_course_from_schema


class ICourseMediator(ABC):

    @abstractmethod
    def create(self, course: Course) -> Course:
        pass

    @abstractmethod
    def list(self) -> list[Course]:
        pass

class CourseMediator(ICourseMediator):
    def __init__(self, service, repository) -> None:
        self.service = service
        self.repository = repository
        self.service.course_mediator = self
        self.repository.course_mediator = self


    def create(self, course: Course) -> Course:
        course_schema: CourseSchema = get_course_to_schema(course)
        course_schema_response = self.repository.course_create(course_schema)
        course_ = get_course_from_schema(course_schema_response)
        return course_

    def list(self) -> list[Course]:
        return []