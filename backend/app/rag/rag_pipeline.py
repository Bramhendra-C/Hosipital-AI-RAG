from app.rag.embeddings import get_embedding_model
from app.rag.vectordb import load_vector_database
from app.rag.prompts import build_prompt
from app.rag.llm import generate_answer
from app.rag.query_classifier import (
    classify_query,
    QueryType,
)
from app.rag.reranker import Reranker


class RAGPipeline:

    def __init__(self):

        print("Loading embedding model...")
        self.embedding_model = get_embedding_model()

        print("Loading vector database...")
        self.vector_db = load_vector_database(
            self.embedding_model
        )

        print("Loading Cross Encoder...")
        self.reranker = Reranker()

        print("RAG Pipeline Ready!")

    # =========================================================
    # Build Sources
    # =========================================================

    def build_sources(self, results):

        seen = set()
        sources = []

        for doc, score in results:

            item = (
                doc.metadata["source"],
                doc.metadata["page"]
            )

            if item not in seen:

                seen.add(item)

                sources.append(item)

        return sources

    # =========================================================
    # Generic Response
    # =========================================================

    def generic_response(self, question: str):

        question_lower = question.strip().lower()

        # Greetings
        if question_lower in [
            "hi",
            "hello",
            "hey",
            "hai",
            "hii"
        ]:

            return (
                "Hello! 👋 I'm the Hospital AI Assistant.\n\n"
                "I can help you find information from the hospital "
                "documents about services, appointments, charges, "
                "registration, departments and patient procedures."
            )

        # Goodbye
        if question_lower in [
            "bye",
            "goodbye",
            "see you",
            "see ya"
        ]:

            return (
                "Goodbye! 👋 Take care.\n\n"
                "Feel free to come back if you have any "
                "hospital-related questions."
            )

        # Thanks
        if question_lower in [
            "thanks",
            "thank you",
            "thankyou"
        ]:

            return (
                "You're welcome! 😊\n\n"
                "I'm happy to help with any hospital-related questions."
            )

        # Who are you?
        if (
            "who are you" in question_lower
            or "what are you" in question_lower
        ):

            return (
                "I'm the Hospital AI Assistant 🏥.\n\n"
                "I help users find information from the uploaded "
                "hospital documents."
            )

        # What can you do?
        if (
            "what can you do" in question_lower
            or "how can you help" in question_lower
            or "what can you help me with" in question_lower
        ):

            return (
                "I can help you find information from the hospital "
                "documents, including:\n\n"
                "• Registration\n"
                "• Appointments\n"
                "• Hospital services\n"
                "• Charges and deposits\n"
                "• Doctors and departments\n"
                "• Smart Card\n"
                "• Blood Bank\n"
                "• Emergency information\n"
                "• Patient procedures"
            )

        # Fallback generic response
        return (
            "Hello! 👋 I'm the Hospital AI Assistant.\n\n"
            "How can I help you with the hospital?"
        )

    # =========================================================
    # Main RAG Pipeline
    # =========================================================

    def ask(self, question: str):

        question = question.strip()

        # -----------------------------------------------------
        # Classify Query
        # -----------------------------------------------------

        query_type = classify_query(question)

        print(
            f"\nQuery Type: {query_type.value}"
        )

        # =====================================================
        # GENERIC QUESTIONS
        # =====================================================

        if query_type == QueryType.GENERIC:

            return {
                "answer": self.generic_response(question),
                "sources": []
            }

        # =====================================================
        # OUT OF SCOPE QUESTIONS
        # =====================================================

        if query_type == QueryType.OUT_OF_SCOPE:

            return {
                "answer": (
                    "I'm designed to answer questions related to "
                    "the uploaded hospital documents.\n\n"
                    "Please ask me something about the hospital."
                ),
                "sources": []
            }

        # =====================================================
        # HOSPITAL QUESTION
        # =====================================================

        # -----------------------------------------------------
        # Step 1: FAISS Retrieval
        # -----------------------------------------------------

        results = self.vector_db.similarity_search_with_score(
            question,
            k=15
        )

        print("\n" + "=" * 90)
        print(f"QUESTION : {question}")
        print("=" * 90)

        print("\nFAISS RESULTS:\n")

        for i, (doc, score) in enumerate(
            results,
            start=1
        ):

            print(
                f"{i:02d}. "
                f"FAISS={score:.4f} | "
                f"Page={doc.metadata['page']} | "
                f"{doc.metadata['source']}"
            )

        # -----------------------------------------------------
        # Step 2: Cross Encoder Re-ranking
        # -----------------------------------------------------

        results = self.reranker.rerank(
            question=question,
            results=results,
            top_k=3
        )

        print("\nRERANKED RESULTS:\n")

        for i, (doc, score) in enumerate(
            results,
            start=1
        ):

            print(
                f"{i:02d}. "
                f"FAISS={score:.4f} | "
                f"Page={doc.metadata['page']} | "
                f"{doc.metadata['source']}"
            )

        print("=" * 90 + "\n")

        # -----------------------------------------------------
        # Step 3: Build Context
        # -----------------------------------------------------

        context = "\n\n".join(
            [
                (
                    f"Page {doc.metadata['page']}\n"
                    f"{doc.page_content}"
                )
                for doc, score in results
            ]
        )

        # -----------------------------------------------------
        # Step 4: Build Prompt
        # -----------------------------------------------------

        prompt = build_prompt(
            context=context,
            question=question
        )

        # -----------------------------------------------------
        # Step 5: Generate Answer
        # -----------------------------------------------------

        answer = generate_answer(prompt)

        normalized_answer = answer.strip().lower()

        if (
            "couldn't find this information" in normalized_answer
            or "could not find this information" in normalized_answer
            or "not present in the provided" in normalized_answer
            or "not mentioned in the provided" in normalized_answer
        ):

            return {
                "answer": answer,
                "sources": []
            }

        return {
            "answer": answer,
            "sources": self.build_sources(results)
}