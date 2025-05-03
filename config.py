import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEBHOOK_API_KEY", "your-secure-api-key")
