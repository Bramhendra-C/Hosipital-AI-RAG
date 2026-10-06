from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        print("Loading Cross Encoder...")

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

        print("Cross Encoder Loaded!")

    def rerank(
        self,
        question,
        results,
        top_k=3
    ):

        pairs = [
            (question, doc.page_content)
            for doc, score in results
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(results, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            item[0]
            for item in ranked[:top_k]
        ]