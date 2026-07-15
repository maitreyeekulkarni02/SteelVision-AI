import os

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///steelvision.db")
