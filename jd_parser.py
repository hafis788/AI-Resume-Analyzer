# jd_parser.py

import pdfplumber

def extract_text_from_jd(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + " "
        return text.strip()
    return ""
