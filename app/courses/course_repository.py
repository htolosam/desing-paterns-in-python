from boto3.dynamodb.conditions import Key

from app.config.databases.dynamodb.database import DatabaseConnect
from app.courses.course_mediator import ICourseMediator
from app.courses.course_model import CourseSchema



class CourseDynaRepository:
    def __init__(self, mediator = None) -> None:
        dbc: DatabaseConnect = DatabaseConnect()
        self.db = dbc.Table('institute')
        self.mediator = mediator

    def course_create(self, course: CourseSchema) -> CourseSchema:
        course_create = self.db.put_item(Item=course.dict())
        print("dato es ::", course_create.get('Item'))
        return course

    def list_course(self) -> list[CourseSchema]:
        response_list = self.db.query(
            KeyConditionExpression=Key('pk').eq('INSTITUTE#1') & Key('sk').begins_with('COURSE#')
        )
        response = response_list.get('Items', [])
        return response
