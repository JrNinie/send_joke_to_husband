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
BLAGUEAPI_TOKEN = os.getenv("BLAGUEAPI_TOKEN")
RANDOM_JOKE_URL = "https://www.blagues-api.fr/api/random"
DISALLOWED_JOKE_TYPES = ["limit", "dark", "blondes"]

# Weather api
CURRENT_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
LOCATION = "Labège"
OPENWEATHER_TOKEN = os.getenv("OPENWEATHER_TOKEN")