from fastapi import FastAPI, File, UploadFile, Response
import tempfile
import shutil
from convert import convert_docx_to_pdf

app = FastAPI()

@app.post("/convert")
async def convert_endpoint(file: UploadFile = File(...)):
    # Save the uploaded DOCX file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx:
        shutil.copyfileobj(file.file, temp_docx)
        temp_docx_path = temp_docx.name
    
    # Convert DOCX to PDF
    pdf_path = temp_docx_path.replace(".docx", ".pdf")
    convert_docx_to_pdf(temp_docx_path, pdf_path)
    
    # Read and return PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()

    return Response(content=pdf_content, media_type="application/pdf")
