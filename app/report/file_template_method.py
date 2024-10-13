from abc import abstractmethod, ABC

from fpdf import FPDF

from app.report.facade_data import FacadeDataStudent
from app.users.student_model import Student


class FileTemplateMethod(ABC):

    def get_data(self):
        facade: FacadeDataStudent = FacadeDataStudent()
        data = facade.list_data_student()
        return data

    @abstractmethod
    def write_data(self, data, path):
        pass

    def create_file(self, path):
        data = self.get_data()
        self.write_data(data, path)
        return path

class TXTFileConcrete(FileTemplateMethod):
    def write_data(self, data: list[Student], file_path):
        with open(file_path, 'w') as file:
            for student in data:
                file.write(f'Nombre Estudiante: {student["name"]}\n')


class PDFFileConcrete(FileTemplateMethod):
    def write_data(self, data: list[Student], file_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for student in data:
            pdf.cell(200, 10, txt=f'Nombre estudiante: {student["name"]} - Email: {student["email"]}', ln=True)
        pdf.output(file_path)