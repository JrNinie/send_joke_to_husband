from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

# Sender
SENDER_MAIL = os.getenv("SENDER_MAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SENDER_HOST = os.getenv("SENDER_HOST")

# Receiver
RECEIVER_MAIL = "xxx@gmail.com"
SUBJECT = "Ta blague du jour, ça avance"

# Joke api
TOKEN = os.getenv("TOKEN")
RANDOM_JOKE_URL = "https://www.blagues-api.fr/api/random"
DISALLOWED_JOKE_TYPES = ["limit","dark", "blondes"]
