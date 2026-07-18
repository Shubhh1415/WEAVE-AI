from services.vector_store import search_documents
from services.gemini_service import get_gemini_response


def ask_rag(question):

    docs = search_documents(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are WEAVE AI.

Answer ONLY using the provided context.

If the answer is not available in the context,
say:

"I couldn't find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    return get_gemini_response(prompt)