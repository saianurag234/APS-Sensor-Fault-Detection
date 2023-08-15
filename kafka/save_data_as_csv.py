from database_config import MongoDBOperation
import pandas as pd
import numpy as np


Database_name = "APS_Database"
Collection_name = "Sensor_Data"

moongdb = MongoDBOperation(Database_name, Collection_name)

data_collection = list(moongdb.collection.find())

data_frame = pd.DataFrame(data_collection)

if '_id' in data_frame.columns:
    data_frame.drop('_id', axis=1, inplace=True)

data_frame.replace({'nan': np.nan}, inplace=True)

data_frame.to_csv("C://Users//hp//Desktop//Kafka//sensor_data.csv")
