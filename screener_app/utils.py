import pdfplumber
import docx

def extract_text_from_pdf(pdf_file):
    text = ''
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

def extract_text_from_docx(docx_file):
    text = ''
    doc = docx.Document(docx_file)
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text
