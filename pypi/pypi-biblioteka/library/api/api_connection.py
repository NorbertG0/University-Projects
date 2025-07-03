import requests
from dotenv import load_dotenv
import os

def get_data():
    load_dotenv()

    API_KEY = os.getenv('API_KEY')
    url = f'https://api.spoonacular.com/recipes/complexSearch?number=100&apiKey={API_KEY}'
    response = requests.get(url)

    return response


