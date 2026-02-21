from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

engine = create_engine(
    url=f"postgresql+psycopg2://{user}:{password}@localhost/{database}"
)
