from pydantic import BaseSettings


class Settings(BaseSettings):
    async_database_url: str = "postgresql+asyncpg://postgres:postgres@db:5432/store"


settings = Settings()