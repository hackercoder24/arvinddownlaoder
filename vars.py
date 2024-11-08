import os

API_ID    = os.environ.get("API_ID", "28400347")
API_HASH  = os.environ.get("API_HASH", "a22d6b94534fe1ad80c63ad0bf9f725c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7512558307:AAH_k9svVmsra47jwR5J5dqwqUSeM-V4sr0") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
