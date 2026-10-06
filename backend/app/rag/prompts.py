def build_prompt(context: str, question: str) -> str:
    """
    Build the prompt sent to Gemini.
    """

    prompt = f"""
You are an AI assistant for Tata Memorial Hospital.

Your job is to answer ONLY from the provided hospital document context.

Rules:
1. Answer ONLY using the provided context.
2. If the answer is not present in the context, reply exactly:
   "I couldn't find this information in the uploaded hospital documents."
3. Do not make up information.
4. Keep the answer clear and concise.
5. At the end of the answer mention the page number if available.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt