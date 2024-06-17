from pydantic import Field

from pydantic_settings import BaseSettings


class KafkaProducerConfig(BaseSettings):
    host: str = Field(alias='KAFKA_HOST')
    port: int = Field(alias='KAFKA_PORT')
    topic: str = Field(alias='KAFKA_TOPIC')

    @property
    def uri(self) -> str:
        return f'{self.host}:{self.port}'


kafka_producer_cfg = KafkaProducerConfig()
