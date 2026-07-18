from langchain_text_splitters import RecursiveCharacterTextSplitter
import pdfplumber
from docx import Document


def load_document(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        text = ""

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        return text

    elif file_name.endswith(".docx"):
        doc = Document(uploaded_file)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    return ""


def split_document(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.create_documents([text])