import pypandoc

def convert_docx_to_pdf(docx_path, pdf_path):
    output = pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)
    return pdf_path
