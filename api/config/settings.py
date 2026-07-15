import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

API_HOST = os.getenv("API_HOST")

API_PORT = int(os.getenv("API_PORT"))

DEBUG = os.getenv("DEBUG") == "True"
