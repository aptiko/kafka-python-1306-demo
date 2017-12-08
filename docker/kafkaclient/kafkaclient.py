import logging
import sys

from kafka import KafkaConsumer


logging.basicConfig(stream=sys.stderr)

kafka_consumer = KafkaConsumer(
    'mytopic',
    bootstrap_servers='kafkaserver',
    group_id='mygroup',
)

kafka_consumer.poll(timeout_ms=300000)
