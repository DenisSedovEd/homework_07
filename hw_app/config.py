from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class DbConfig(BaseSettings):
    echo: bool = False
    pool_size: int = 50
    max_overflow: int = 0
    dialect: str = "postgresql"
    sync_engine: str = "psycopg"
    async_engine: str = "asyncpg"
    mok_data_from_api = "https://jsonplaceholder.typicode.com/users"

    host: str
    port: str
    user: str
    password: str
    database: str

    def build_url(self, engine: str) -> str:
        return f"{self.dialect}+{engine}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    @property
    def url_sync(self) -> str:
        return self.build_url(self.sync_engine)

    @property
    def url_async(self) -> str:
        return self.build_url(self.async_engine)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BLOG_APP__",
        env_nested_delimiter="__",
        case_sensitive=False,
        env_file=(
            BASE_DIR / ".env.template",
            BASE_DIR / ".env",
        ),
    )
    foo: str = "bar"
    db: DbConfig


settings = Settings()

if __name__ == "__main__":

    print(Settings().model_dump_json(indent=2))
