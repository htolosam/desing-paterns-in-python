from boto3.dynamodb.conditions import Key
from pydantic import BaseModel

from app.config.databases.dynamodb.database import DatabaseConnect


class DynaRepository:
    def __init__(self) -> None:
        dbc: DatabaseConnect = DatabaseConnect()
        self.db = dbc.Table('institute')

    def create(self, item: BaseModel) -> BaseModel:
        item_create = self.db.put_item(Item=item.dict())
        print("dato es ::", item_create.get('Item'))
        return item

    def list_by_key(self, pk_data: str, sk_data: str) -> list[BaseModel]:
        response_list = self.db.query(
            KeyConditionExpression=Key('pk').eq(pk_data) & Key('sk').begins_with(sk_data)
        )
        response = response_list.get('Items', [])
        return response

    def delete(self, pk_data: str, sk_data: str) -> None:
        self.db.delete_item(pk_data, sk_data)
