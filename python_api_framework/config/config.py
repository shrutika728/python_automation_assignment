from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """Configuration class to manage environment variables."""
    BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")
    TIMEOUT = int(os.getenv("TIMEOUT", 10))

