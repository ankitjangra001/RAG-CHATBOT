from app.services.pdf_services import read_pdf
from app.services.chunk_service import split_documents
from fastapi import FastAPI
import os
from fastapi import FastAPI, UploadFile, File
from app.services.embeddings_service import create_vector_store
from app.services.chat_service import ask_pdf
from app.models.question import QuestionRequest
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.pdf_services import read_pdf
from backend.app.services.chunk_service import split_documents
from backend.app.services.embeddings_service import create_vector_store
from backend.app.services.chat_service import ask_pdf
from backend.app.models.question import QuestionRequest

app = FastAPI(
    title="RAG PDF Chatbot API",
    description="Backend API for AI PDF Chatbot",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

@app.get("/")
def home():
    return {
        "message": "Welcome to RAG PDF Chatbot API"
    }
@app.get("/health")
def health():
    return {
        "status": "Server Running",
        "version": "1.0.0"
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    documents = read_pdf(file_path)
    chunks = split_documents(documents)
    vector_db = create_vector_store(chunks)

    return {

        "filename":file.filename,

        "pages":len(documents),

        "chunks": len(chunks),

        "status": "Vector Database Created Successfully"    
    }

@app.post("/chat")
def chat(data: QuestionRequest):

    answer = ask_pdf(data.question)

    return {

        "answer": answer

    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)