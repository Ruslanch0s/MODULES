import json

import pika
from pika.exceptions import AMQPConnectionError, StreamLostError

from backoff import backoff
from config import rabbitmq_cfg
from logger import logger


@backoff(exceptions=(AMQPConnectionError,))
def connect_to_rabbitmq():
    logger.info(
        f'Connecting to RabbitMQ {rabbitmq_cfg.host} {rabbitmq_cfg.port}')
    credentials = pika.PlainCredentials(rabbitmq_cfg.username,
                                        rabbitmq_cfg.password)
    _connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=rabbitmq_cfg.host, port=rabbitmq_cfg.port,
            credentials=credentials
        )
    )
    _channel = _connection.channel()
    logger.info('Connected')
    # create queue
    channel.queue_declare(queue=rabbitmq_cfg.queue, durable=True)
    return _connection, _channel


connection, channel = connect_to_rabbitmq()


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


if __name__ == '__main__':
    data = {
        'tag_id': 123,
        'antenna_id': 321,
    }
    try:
        channel.basic_publish(
            exchange='',
            routing_key=rabbitmq_cfg.queue,
            body=json.dumps(data).encode('utf-8'),
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
                # сохранить на диск
            )
        )
    except StreamLostError:
        logger.warning('Stream connection lost. Reconnecting...')
        connection, channel = connect_to_rabbitmq()
