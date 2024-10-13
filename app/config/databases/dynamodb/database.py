import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from pydantic import BaseModel


# Singleton para la conección a la base de datos
class DatabaseConnect:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            try:
                cls.instance = super(DatabaseConnect, cls).__new__(cls)
                # Crear una instancia de la conexión a DynamoDB
                cls.instance = boto3.resource('dynamodb', region_name='us-east-2')
                print("Conexión a DynamoDB establecida.")
            except (NoCredentialsError, PartialCredentialsError) as e:
                print("Error en las credenciales de AWS: ", e)
                cls.instance = None
        return cls.instance

    def get_db(cls):
        return cls.instance

    def get_table(self, table_name):
        # Retorna una referencia a la tabla solicitada
        return self.dynamodb.Table(table_name)

# def get_db() -> Generator[Session, None, None]:
#     db = DatabaseConnect()
#     db_session = db.session()  # type: ignore
#     try:
#         yield db_session
#     finally:
#         db_session.close()





