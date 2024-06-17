from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    astra_db_client_id: str = Field("ASTRA_DB_CLIENT_ID")
    astra_db_client_secret: str = Field("ASTRA_DB_CLIENT_SECRET")
    
    class Config:
        env_file = '.env'

@lru_cache
def get_settings():
    return Settings()