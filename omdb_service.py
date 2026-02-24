import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"


def fetch_movies(title):
    params = {
        "apikey": API_KEY,
        "s": title
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("Response") == "True":
        return data["Search"]
    else:
        return []