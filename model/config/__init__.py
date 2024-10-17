import os


class Config:
    # Environment variables
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
