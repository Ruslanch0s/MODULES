#!/bin/bash

KAFKA_BIN="/opt/bitnami/kafka/bin"
BROKER_LIST="kafka-0:9092,kafka-1:9092,kafka-2:9092"

# Создание топика
$KAFKA_BIN/kafka-topics.sh --create --topic test_topic --partitions 3 --replication-factor 3 --config min.insync.replicas=2 --config cleanup.policy=delete --config retention.ms=604800000 --bootstrap-server $BROKER_LIST

# Создание топика с увеличенным временем хранения сообщений
# --config retention.ms=604800000
# Создание топика с ограничением на размер журнала
# --config max.log.bytes=1073741824
# Создание топика с настройками для очистки данных
# --config cleanup.policy=delete
# Создание топика с минимальными синхронными репликами и другими пользовательскими настройками
# --config min.insync.replicas=2

echo "Все топики успешно созданы"
