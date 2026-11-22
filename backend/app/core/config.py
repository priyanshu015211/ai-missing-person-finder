from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or backend/.env."""

    app_name: str = "AI Missing Person Finder API"
    app_version: str = "0.1.0"
    environment: str = "development"
    database_url: str = (
        "mysql+pymysql://mpf_app:CHANGE_ME@127.0.0.1:3306/"
        "missing_person_finder?charset=utf8mb4"
    )
    frontend_origins: str = (
        "http://localhost:5173,http://127.0.0.1:5173"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        """Return the configured, non-empty browser origins."""
        return [
            origin.strip()
            for origin in self.frontend_origins.split(",")
            if origin.strip()
        ]


settings = Settings()
