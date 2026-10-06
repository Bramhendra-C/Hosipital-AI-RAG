import fitz
from langchain_core.documents import Document

def parse_pdf(pdf_path):

    pdf = fitz.open(pdf_path)

    documents = []

    for page_number in range(pdf.page_count):

        page = pdf.load_page(page_number)

        text = page.get_text("text")

        doc = Document(
            page_content=text,
            metadata={
                "page": page_number + 1,
                "source": pdf_path.name
            }
        )

        documents.append(doc)

    pdf.close()

    return documents