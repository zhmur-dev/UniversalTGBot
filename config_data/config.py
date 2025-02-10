from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Базовые настройки приложения
    """

    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str

    GOOGLE_ACCOUNT_JSON: str
    GOOGLE_TABLE_ID: str

    @property
    def db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:5432/{self.DB_NAME}'

    # Настройки для использования переменных из ..env
    model_config = SettingsConfigDict(
        env_file='../.env', env_file_encoding='utf-8', extra='allow')


settings = Settings()
