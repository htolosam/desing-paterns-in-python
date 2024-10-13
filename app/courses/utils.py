from app.courses.course_model import CourseSchema, Course


def get_course_to_schema(course: Course) -> CourseSchema:
    course_schema: CourseSchema = CourseSchema(pk="", sk="", name=course.name)
    course_schema.add_prefix(course.id)
    return course_schema

def get_course_from_schema(course_schema: CourseSchema) -> Course:
    course: Course = Course(id=course_schema.pk.split("#")[1], name=course_schema.name)
    return course