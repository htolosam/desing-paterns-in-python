from boto3.dynamodb.conditions import Key

from app.config.databases.dynamodb.database import DatabaseConnect
from app.users.student_model import Student


class StudentDynaRepository:
    def __init__(self) -> None:
        dbc: DatabaseConnect = DatabaseConnect()
        self.db = dbc.Table('institute')

    def create_student(self, student: Student) -> Student:
        student_create = self.db.put_item(Item=student.dict())
        print(student_create.get('Item'))
        return student

    def list_students(self) -> list[Student]:
        response_list = self.db.query(
            KeyConditionExpression=Key('pk').eq('INSTITUTE#1') & Key('sk').begins_with('STUDENT#')
        )
        response = response_list.get('Items', [])
        return response
