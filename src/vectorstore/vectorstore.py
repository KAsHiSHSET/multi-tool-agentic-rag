"""Vector Store using FAISS + HuggingFace Embeddings"""

from typing import List

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.config.config import Config


class VectorStore:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL
        )

        self.vectorstore = None
        self.retriever = None

    def create_vectorstore(self, documents: List[Document]):

        self.vectorstore = FAISS.from_documents(
            documents,
            self.embedding
        )

        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

    def get_retriever(self):

        if self.retriever is None:
            raise ValueError("Vector store not initialized.")

        return self.retriever