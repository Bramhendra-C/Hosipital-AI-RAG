from fastapi import APIRouter

from app.models.chat_models import (
    ChatRequest,
    ChatResponse,
    Source,
)

from app.rag.rag_pipeline import RAGPipeline

router = APIRouter()

# Load once when the server starts
pipeline = RAGPipeline()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = pipeline.ask(request.question)

    sources = [
        Source(
            source=source,
            page=page
        )
        for source, page in result["sources"]
    ]

    return ChatResponse(
        answer=result["answer"],
        sources=sources
    )