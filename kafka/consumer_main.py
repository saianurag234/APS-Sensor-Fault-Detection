import argparse
from uuid import uuid4
from kafka_config import sasl_conf, schema_config
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka import Consumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
import pandas as pd
from typing import List
from schema_generate import Sensor, instance_to_dict
from database_config import MongoDBOperation


Database_name = "APS_Database"
Collection_name = "Sensor_Data"
file_path = "C:/Users/hp/Desktop/Kafka/sample_data/kafka-sensor-topic/sensor_data.csv"


def consumer_using_sample_file(topic, file_path):
    schema_str = Sensor.generate_schema_from_data(file_path=file_path)
    json_deserializer = JSONDeserializer(schema_str,
                                         from_dict=Sensor.dict_to_object)

    consumer_conf = sasl_conf()
    consumer_conf.update({
        'group.id': 'group1',
        'auto.offset.reset': "earliest"})

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    mongodb = MongoDBOperation(
        Database_name=Database_name, Collection_name=Collection_name)

    records = []
    x = 0
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            record: Sensor = json_deserializer(
                msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))

            if record is not None:
                records.append(record.to_dict())
                if x % 100 == 0:
                    mongodb.collection.insert_many(records)
                    records = []
            x = x + 1
        except KeyboardInterrupt:
            break

    consumer.close()


if __name__ == '__main__':
    consumer_using_sample_file("aps-sensor-data", file_path=file_path)
