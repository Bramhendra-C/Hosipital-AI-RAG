from app.rag.bm25_retriever import BM25Retriever
from app.rag.rrf import reciprocal_rank_fusion


class HybridRetriever:

    def __init__(self, vector_db):

        self.faiss = vector_db.as_retriever(
            search_kwargs={"k": 5}
        )

        docs = vector_db.docstore._dict.values()

        self.bm25 = BM25Retriever(
            list(docs)
        )

    def retrieve(self, query):

        semantic = self.faiss.invoke(query)

        keyword = self.bm25.retrieve(query)

        return reciprocal_rank_fusion(
            semantic,
            keyword
        )[:5]