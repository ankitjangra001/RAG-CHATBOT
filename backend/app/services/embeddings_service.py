from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS



embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


def create_vector_store(chunks):

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )
    vector_db.save_local("vector_db")

    return vector_db