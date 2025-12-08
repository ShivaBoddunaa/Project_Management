import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
db_link = os.getenv("database_url")
api_key = os.getenv('api')

db = create_client(db_link,api_key)


# import os
# from supabase import create_client

# db_link = os.getenv("SUPABASE_URL")
# api_key = os.getenv("SUPABASE_KEY")

# if not db_link or not api_key:
#     raise Exception("Supabase environment variables missing!")

# db = create_client(db_link, api_key)
