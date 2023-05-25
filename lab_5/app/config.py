from typing import Optional, Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_PORT: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_URI: Optional[PostgresDsn] = None

    @validator("POSTGRES_URI", pre=True, allow_reuse=True)
    def assemble_db_connection(cls, v: Optional[str], values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file = '.env'


settings = Settings()
