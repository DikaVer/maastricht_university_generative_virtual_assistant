import os

print("Current path: ", os.getcwd())
# Load local environment variables
from dotenv import load_dotenv

print("Environment variables are loaded = ", load_dotenv())

# Environment variables
mistral_api_key = os.getenv("MISTRAL_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
GOOGLE_PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
print("Mistral API key: ", mistral_api_key)
print("OpenAI API key: ", openai_api_key)
print("Google project ID: ", GOOGLE_PROJECT_ID)
print("Huggingface API key: ", huggingface_api_key)

os.environ["HF_TOKEN"] = huggingface_api_key

# Set up Google Cloud SDK
# gcloud config set project $GOOGLE_PROJECT_ID
# gcloud auth application-default login
