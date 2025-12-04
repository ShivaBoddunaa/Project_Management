import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("db_link")
api_key = os.getenv('api')
