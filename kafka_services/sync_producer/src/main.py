import json
import random
import time

from kafka import KafkaProducer

from config import kafka_cfg


# Функция для сериализации данных в формат JSON
def json_serializer(data):
    return json.dumps(data).encode('utf-8')


# Инициализация Kafka-продюсера
producer = KafkaProducer(
    bootstrap_servers=[kafka_cfg.uri],
    value_serializer=json_serializer
)


# Функция для генерации случайного сообщения
def generate_message():
    return {'key': random.randint(0, 100), 'value': random.random()}


# Бесконечный цикл для отправки сообщений
try:
    while True:
        message = generate_message()
        future = producer.send(kafka_cfg.topic, value=message)

        try:
            result = future.get(
                timeout=10)  # Ожидание завершения отправки сообщения
            print(f'Message sent successfully: {result}')
        except Exception as e:
            print(f'Failed to send message: {e}')

        # Задержка в 1 секунду перед отправкой следующего сообщения
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping producer...")
finally:
    # Закрытие продюсера при завершении работы
    producer.close()
