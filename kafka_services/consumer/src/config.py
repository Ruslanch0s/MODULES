from pydantic import Field

from pydantic_settings import BaseSettings


class KafkaConfig(BaseSettings):
    servers: list = Field(alias='KAFKA_SERVERS')
    topic: str = Field(alias='KAFKA_TOPIC')
    group_id: str = Field(alias='KAFKA_GROUP_ID')


kafka_cfg = KafkaConfig()
