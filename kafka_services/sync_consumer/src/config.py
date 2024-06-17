from pydantic import Field

from pydantic_settings import BaseSettings


class KafkaConsumerConfig(BaseSettings):
    host: str = Field(alias='KAFKA_HOST')
    port: int = Field(alias='KAFKA_PORT')
    topic: str = Field(alias='KAFKA_TOPIC')
    group_id: str = Field(alias='KAFKA_GROUP_ID')

    @property
    def uri(self) -> str:
        return f'{self.host}:{self.port}'


kafka_consumer_cfg = KafkaConsumerConfig()
