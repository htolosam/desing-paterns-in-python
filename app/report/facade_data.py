from app.users.student_dynamo_repository import StudentDynaRepository


class FacadeDataStudent:

    def __init__(self):
        self.repository = StudentDynaRepository()

    def list_data_student(self):
        return self.repository.list_students()