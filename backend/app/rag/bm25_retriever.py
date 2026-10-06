from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, documents):

        self.documents = documents

        self.corpus = [
            doc.page_content.lower().split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query, k=5):

        scores = self.bm25.get_scores(
            query.lower().split()
        )

        ranked = sorted(
            zip(scores, self.documents),
            reverse=True,
            key=lambda x: x[0]
        )

        return [doc for _, doc in ranked[:k]]