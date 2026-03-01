import pandas as pd
import json

class GetData:
    def __init__(self, path):
        self.df = pd.read_csv(path, sep='\\s+')
        self.json_data = self.df.to_json(orient="records", indent=4)

    def get_simple_data(self):
        return json.loads(self.json_data)
    
    def define_key(self, key_value):
        if isinstance(self.json_data, str):
            object_data = json.loads(self.json_data)
        else:
            object_data = self.json_data

        retrieve_value = []
        for data in object_data:
            retrieve_value.append(data[key_value])

        return retrieve_value