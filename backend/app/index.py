from parser import parse_pdf
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
