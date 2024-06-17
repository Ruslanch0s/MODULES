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


# Колбэк для успешной отправки сообщения
def on_send_success(record_metadata):
    print(f'Message sent successfully to {record_metadata.topic} partition'
          f' {record_metadata.partition} offset {record_metadata.offset}')


# Колбэк для ошибки отправки сообщения
def on_send_error(excp):
    print(f'Failed to send message: {excp}')


# Бесконечный цикл для отправки сообщений
try:
    while True:
        message = generate_message()
        # В этом случае мы отправляем сообщение асинхронно и добавляем колбэки
        # для обработки результата отправки.
        producer.send(kafka_cfg.topic, value=message).add_callback(
            on_send_success).add_errback(on_send_error)

        # Задержка в 1 секунду перед отправкой следующего сообщения
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping producer...")
finally:
    # Закрытие продюсера при завершении работы
    producer.close()
