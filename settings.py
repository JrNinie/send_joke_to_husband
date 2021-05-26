from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(),override=True)

# Sender
SENDER_ACCOUNT=os.getenv("SENDER_ACCOUNT")
SENDER_PASSWORD=os.getenv("SENDER_PASSWORD")
SENDER_HOST=os.getenv("SENDER_HOST")


