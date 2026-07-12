from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

llm = ChatOllama(model="gemma:2b")


def ask_pdf(question):

    vector_db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content