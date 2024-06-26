from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresConfig(BaseSettings):
    host: str = Field(alias='POSTGRES_HOST')
    port: int = Field(alias='POSTGRES_PORT')
    user: str = Field(alias='POSTGRES_USER')
    password: str = Field(alias='POSTGRES_PASSWORD')
    database: str = Field(alias='POSTGRES_DB')

    @property
    def uri(self) -> str:
        return (f'postgresql://{self.user}:{self.password}@'
                f'{self.host}:{self.port}/{self.database}')


pg_cfg = PostgresConfig()
