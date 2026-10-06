from langchain_community.vectorstores import FAISS
from app.config import VECTOR_DB_PATH


def build_vector_database(chunks, embedding_model):
    """
    Build a FAISS vector database from chunks.
    """

    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_db



def save_vector_database(vector_db):

    vector_db.save_local(VECTOR_DB_PATH)


def load_vector_database(embedding_model):

    vector_db = FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_db