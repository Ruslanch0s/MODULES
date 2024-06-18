import json

from kafka import KafkaConsumer

from config import kafka_cfg
from logger import logger


def json_serializer(data):
    return json.loads(data.decode('utf-8'))


# Инициализация Kafka-консюмера
consumer = KafkaConsumer(
    kafka_cfg.topic,  # Тема, из которой читаем сообщения
    bootstrap_servers=kafka_cfg.servers,
    auto_offset_reset='earliest',
    # Начинаем читать с самого начала, если нет смещений
    enable_auto_commit=True,
    # Автоматически подтверждаем обработанные сообщения
    group_id=kafka_cfg.group_id,
    # Идентификатор группы консюмеров (у них общий offset)
    value_deserializer=json_serializer)

# Бесконечный цикл для чтения сообщений
try:
    for message in consumer:
        logger.info(f"Received message: {message.value}")
except KeyboardInterrupt:
    logger.error("Stopping consumer...")
finally:
    # Закрытие консюмера при завершении работы
    consumer.close()
