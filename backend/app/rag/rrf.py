def reciprocal_rank_fusion(*rankings, k=60):

    scores = {}

    for ranking in rankings:

        for rank, doc in enumerate(ranking):

            doc_id = (
                doc.metadata["source"],
                doc.metadata["page"]
            )

            scores.setdefault(doc_id, {
                "doc": doc,
                "score": 0
            })

            scores[doc_id]["score"] += 1 / (k + rank + 1)

    ranked = sorted(
        scores.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    return [item["doc"] for item in ranked]