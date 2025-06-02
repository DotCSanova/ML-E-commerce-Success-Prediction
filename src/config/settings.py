# Configuration settings for the project
import os

API_KEY = os.getenv("API_KEY", "default_key")
MODEL_PATH = os.getenv("MODEL_PATH", "./models/model.pkl")
