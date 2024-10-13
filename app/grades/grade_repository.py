from boto3.dynamodb.conditions import Key

from app.config.databases.dynamodb.database import DatabaseConnect
from app.grades.grades_model import GradeSchema, Grade


class GradeDynaRepository:
    def __init__(self) -> None:
        super().__init__()
        dbc: DatabaseConnect = DatabaseConnect()
        self.db = dbc.Table('institute')


    def list_by_key(self, pk_key: str, pk_data: str, sk_key: str, sk_data: str) -> list[GradeSchema]:
        grades = self.db.query(
            IndexName='GradeIndex',
            KeyConditionExpression=Key(pk_key).eq(pk_data) & Key(sk_key).begins_with(sk_data)
        )
        response = grades.get('Items', [])
        return response

    def create_grade(self, grade: GradeSchema) -> GradeSchema:
        grade_data = self.db.put_item(Item=grade.dict())
        return grade_data
