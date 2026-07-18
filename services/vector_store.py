import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Persistent database location
CHROMA_PATH = "database/chroma_db"


def get_embeddings():
    """
    Load HuggingFace embedding model.
    This runs locally and does not require a Google API.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def get_vector_store():
    """
    Create or load the persistent Chroma vector database.
    """
    os.makedirs(CHROMA_PATH, exist_ok=True)

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
    )

    return vector_store


def add_documents(documents):
    """
    Add document chunks to ChromaDB.
    """
    vector_store = get_vector_store()
    vector_store.add_documents(documents)


def search_documents(query, k=4):
    """
    Search the vector database.
    """
    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query=query,
        k=k,
    )

    return results


def delete_vector_store():
    """
    Delete all vectors from the database.
    """
    if os.path.exists(CHROMA_PATH):
        import shutil
        shutil.rmtree(CHROMA_PATH)
        os.makedirs(CHROMA_PATH)