
import argparse
from uuid import uuid4
from kafka_config import sasl_conf, schema_config
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import pandas as pd
from typing import List
from schema_generate import Sensor, instance_to_dict


file_path = "C:/Users/hp/Desktop/Kafka/sample_data/kafka-sensor-topic/sensor_data.csv"


def delivery_report(err, msg):

    if err is not None:
        print(
            "Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


def product_data_using_file(topic, file_path):

    print(f"Topic: {topic} file_path:{file_path}")

    schema_str = Sensor.generate_schema_from_data(file_path=file_path)
    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    string_serializer = StringSerializer('utf_8')
    json_serializer = JSONSerializer(
        schema_str, schema_registry_client, instance_to_dict)
    producer = Producer(sasl_conf())

    print("Producing user records to topic {}. ^C to exit.".format(topic))

    producer.poll(0.0)

    try:
        for instance in Sensor.get_data(file_path=file_path):
            print(instance)

            producer.produce(topic=topic,
                             key=string_serializer(
                                 str(uuid4()), instance.to_dict()),
                             value=json_serializer(
                                 instance, SerializationContext(topic, MessageField.VALUE)),
                             on_delivery=delivery_report)
            print("\nFlushing records...")
            producer.flush()
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid input, discarding record...")
        pass


if __name__ == '__main__':
    product_data_using_file("aps-sensor-data", file_path=file_path)
