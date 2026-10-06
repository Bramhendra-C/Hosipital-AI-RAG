from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load the embedding model.
    """

    model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    return model


