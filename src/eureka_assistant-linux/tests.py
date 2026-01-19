import dotenv
import os
from importlib import resources
from dotenv import load_dotenv, find_dotenv, set_key

load_dotenv()
dotenv_path = find_dotenv()

API_KEY = os.getenv("API_KEY")
print(API_KEY)
