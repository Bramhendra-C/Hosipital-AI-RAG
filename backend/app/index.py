'''from parser import parse_pdf
from chunker import chunk_documents
from embeddings import get_embedding_model
from vectordb import (
    build_vector_database,
    save_vector_database
)

from app.config import PDF_PATH


def main():

    print("=" * 60)
    print("🏥 Hospital AI Assistant - Knowledge Indexer")
    print("=" * 60)

    print("\n[1/5] Parsing PDF...")
    documents = parse_pdf(PDF_PATH)
    print(f"✓ Parsed {len(documents)} pages")

    print("\n[2/5] Chunking...")
    chunks = chunk_documents(documents)
    print(f"✓ Created {len(chunks)} chunks")

    print("\n[3/5] Loading Embedding Model...")
    embedding_model = get_embedding_model()
    print("✓ Model Loaded")

    print("\n[4/5] Building Vector Database...")
    vector_db = build_vector_database(chunks, embedding_model)
    print("✓ Vector Database Created")

    print("\n[5/5] Saving Vector Database...")
    save_vector_database(vector_db)
    print("✓ Saved Successfully")

    print("\n🎉 Knowledge Base Ready!")


if __name__ == "__main__":
    main()

'''

from pathlib import Path

from app.rag.parser import parse_pdf
from app.rag.chunker import chunk_documents
from app.rag.embeddings import get_embedding_model
from app.rag.vectordb import (
    build_vector_database,
    save_vector_database
)

from app.config import RAW_DIR, DATA_DIR


def main():

    print("=" * 70)
    print("Hospital AI Assistant - Knowledge Indexer")
    print("=" * 70)

    # ---------------------------------------------------------
    # 1. Find all PDF files
    # ---------------------------------------------------------

    pdf_files = []

    # Original hospital booklet
    hospital_pdf = RAW_DIR / "TMH_Patient_Booklet_2026.pdf"

    if hospital_pdf.exists():
        pdf_files.append(hospital_pdf)
    else:
        print(f"\nWARNING: Hospital booklet not found:")
        print(hospital_pdf)

    # Medical knowledge PDFs
    medical_knowledge_dir = DATA_DIR / "medical_knowledge"

    if medical_knowledge_dir.exists():
        medical_pdfs = sorted(
            medical_knowledge_dir.glob("*.pdf")
        )
        pdf_files.extend(medical_pdfs)

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files were found to index."
        )

    print(f"\nFound {len(pdf_files)} PDF files:")

    for pdf_path in pdf_files:
        print(f"  - {pdf_path.name}")

    # ---------------------------------------------------------
    # 2. Parse all PDFs
    # ---------------------------------------------------------

    print("\n[1/5] Parsing PDFs...")

    all_documents = []

    for pdf_path in pdf_files:

        print(f"\n  Parsing: {pdf_path.name}")

        documents = parse_pdf(pdf_path)

        print(f"  Pages: {len(documents)}")

        all_documents.extend(documents)

    print(f"\nTotal pages loaded: {len(all_documents)}")

    # ---------------------------------------------------------
    # 3. Chunk all documents
    # ---------------------------------------------------------

    print("\n[2/5] Chunking documents...")

    chunks = chunk_documents(all_documents)

    print(f"Total chunks created: {len(chunks)}")

    # ---------------------------------------------------------
    # 4. Load embedding model and build FAISS
    # ---------------------------------------------------------

    print("\n[3/5] Loading embedding model...")

    embedding_model = get_embedding_model()

    print("Embedding model loaded.")

    print("\n[4/5] Building FAISS vector database...")

    vector_db = build_vector_database(
        chunks,
        embedding_model
    )

    print("FAISS vector database created.")

    # ---------------------------------------------------------
    # 5. Save FAISS database
    # ---------------------------------------------------------

    print("\n[5/5] Saving vector database...")

    save_vector_database(vector_db)

    print("\n" + "=" * 70)
    print("Knowledge Base Ready!")
    print("=" * 70)

    print(f"\nPDF files indexed : {len(pdf_files)}")
    print(f"Pages indexed     : {len(all_documents)}")
    print(f"Chunks indexed    : {len(chunks)}")

    print("\nSources:")

    for pdf_path in pdf_files:
        print(f"  - {pdf_path.name}")

    print("\nFAISS location:")
    print(DATA_DIR / "vectorstore" / "faiss_index")


if __name__ == "__main__":
    main()