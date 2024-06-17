from kafka import KafkaConsumer
import json
from config import kafka_cfg


def json_serializer(data):
    return json.loads(data.decode('utf-8'))


# Инициализация Kafka-консюмера
consumer = KafkaConsumer(
    kafka_cfg.topic,  # Тема, из которой читаем сообщения
    bootstrap_servers=[kafka_cfg.uri],
    auto_offset_reset='earliest',
    # Начинаем читать с самого начала, если нет смещений
    enable_auto_commit=True,
    # Автоматически подтверждаем обработанные сообщения
    group_id='rfid_group',  # Идентификатор группы консюмеров
    value_deserializer=json_serializer)

# Бесконечный цикл для чтения сообщений
try:
    for message in consumer:
        print(f"Received message: {message.value}")
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    # Закрытие консюмера при завершении работы
    consumer.close()
