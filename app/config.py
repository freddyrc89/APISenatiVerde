from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "u911718531_senati"
    DB_PASSWORD: str = "S3nati123"
    DB_HOST: str = "srv1851.hstgr.io"
    DB_PORT: str = "3306"
    DB_NAME: str = "u911718531_moviles20251"

    class Config:
        env_file = ".env"

settings = Settings()
