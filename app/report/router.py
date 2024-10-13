from fastapi import APIRouter
from starlette.responses import FileResponse

from app.report.file_template_method import TXTFileConcrete, PDFFileConcrete

router = APIRouter()

@router.get("/txt")
async def get_txt():
    path = 'report_file.txt'
    txt_file = TXTFileConcrete()
    txt_file.create_file(path)
    return FileResponse(path, media_type='text/plain', filename="report_file.txt")


@router.get("/pdf")
async def get_pdf():
    pdf_file = PDFFileConcrete()
    file_path = pdf_file.create_file("report_file.pdf")
    return FileResponse(file_path, filename=f"report_file.pdf", media_type='application/pdf')