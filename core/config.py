from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    db_url: str = os.environ.get("DB_URL")
    # db_echo: bool = False
    db_echo: bool = True


settings = Settings()
