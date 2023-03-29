import requests
from dotenv import load_dotenv
import os


load_dotenv()
GTF_KEY = os.getenv("GTF_KEY")



url = "https://api.resrobot.se/gtfs/sweden.zip?key={GTF_KEY}"

response = requests.get(url)

print(response)