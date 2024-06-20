import random
import time
from time import sleep

from pika import BlockingConnection, ConnectionParameters, PlainCredentials, \
    DeliveryMode, BasicProperties
from pika.exchange_type import ExchangeType

EXCHANGE_NAME = 'direct_logs'

if __name__ == '__main__':
    credentials = PlainCredentials('root', 'admin')
    connection = BlockingConnection(
        ConnectionParameters(host='localhost', credentials=credentials)
    )
    channel = connection.channel()

    # создадим очередь
    # durable=True будет сохранять сообщения даже если consumer не доступен
    channel.queue_declare(queue='test_queue', durable=True)

    # что бы точно отправить в конкретную очередь, то exchange=''
    while 1:
        channel.basic_publish(
            exchange='',
            routing_key='test_queue',
            body='Hello World!',
            properties=BasicProperties(
                delivery_mode=DeliveryMode.Persistent  # сохранить на диск
            )
        )
        print(" [x] Sent 'Hello World!'")
        time.sleep(1)
    connection.close()

    # channel.exchange_declare(
    #     exchange=EXCHANGE_NAME, exchange_type=ExchangeType.direct
    # )
    #
    # counter = 0
    # while True:
    #     counter += 1
    #     message_type = random.choice(['error', 'warning', 'info'])
    #     message_body = f'Сообщение {message_type}! {counter}'
    #     channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=message_type,
    #                           body=message_body)
    #     print(f'[✅] {message_body}')
    #     sleep(1)
