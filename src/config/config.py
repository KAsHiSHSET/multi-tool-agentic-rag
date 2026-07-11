"""Configuration module"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env
load_dotenv()


class Config:

    # API Key
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Model
    MODEL_NAME = "llama-3.3-70b-versatile"

    # Embedding Model
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # Chunking
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    # Default URLs
    DEFAULT_URLS = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
     ]

    @classmethod
    def get_llm(cls):
        return ChatGroq(
            groq_api_key=cls.GROQ_API_KEY,
            model=cls.MODEL_NAME,
            temperature=0,
        )