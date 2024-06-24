from pydantic import Field

from pydantic_settings import BaseSettings


class RabbitMqConfig(BaseSettings):
    username: str = Field(alias='RABBITMQ_USERNAME')
    password: str = Field(alias='RABBITMQ_PASSWORD')
    host: str = Field(default='localhost', alias='RABBITMQ_HOST')
    port: int = Field(default=5672, alias='RABBITMQ_PORT')
    queue: str = Field(alias='RABBITMQ_QUEUE')


rabbitmq_cfg = RabbitMqConfig()
