import os
from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-key")
MODEL_NAME = "gpt-4o-mini"
DB_NAME = "vector_db"
DOCS_PATH = "Multimodal_Content_Retriever/Dataset/"
