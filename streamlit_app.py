import streamlit as st

from backend.app.services.pdf_services import read_pdf
from backend.app.services.chat_service import ask_pdf


st.title("RAG PDF Chatbot")

pdf = st.file_uploader("Upload PDF")

if pdf:
    st.success(f"Uploaded: {pdf.name}")