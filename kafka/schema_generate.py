
import pandas as pd
import json


class Sensor:

    def __init__(self, record: dict):
        for k, v in record.items():
            setattr(self, k, v)

    def dict_to_object(data: dict, ctx):
        print(data, ctx)
        return Sensor(record=data)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def get_data(cls, file_path):
        chunk_df = pd.read_csv(file_path, chunksize=10)
        n_row = 0
        for df in chunk_df:
            for data in df.values:
                sensor = Sensor(dict(zip(df.columns, list(map(str, data)))))
                n_row += 1
                yield sensor

    @classmethod
    def generate_schema_from_data(cls, file_path):
        columns = next(pd.read_csv(file_path, chunksize=10)).columns

        schema = dict()
        schema.update({
            "$id": "http://example.com/myURI.schema.json",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "additionalProperties": False,
            "description": "Sample schema to help you get started.",
            "properties": dict(),
            "title": "SampleRecord",
            "type": "object"})
        for column in columns:
            schema["properties"].update(
                {
                    f"{column}": {
                        "description": f"Sensor {column} ",
                        "type": "string"
                    }
                }
            )

        schema = json.dumps(schema)

        print(schema)
        return schema

    def __str__(self):
        return f"{self.__dict__}"


def instance_to_dict(instance: Sensor, ctx):
    return instance.to_dict()
