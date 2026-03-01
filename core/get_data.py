import pandas as pd
import json
from pandas.errors import EmptyDataError
from termcolor import colored

class GetData:
    def __init__(self, path):
        try:
            self.df = pd.read_csv(path, sep='\\s+')
            if self.df.empty:
                print(colored(f"Error Occured. No data found on {path}", "red"))
                self.json_data = "[]"
            else:
                self.json_data = self.df.to_json(orient="records", indent=4)

        except EmptyDataError:
            print(colored(f"Error Occured. No data found on {path}", "red"))
            self.json_data = "[]"
            self.df = pd.DataFrame()

        except FileNotFoundError:
            print(colored(f"{path} does not exist", "red"))
            self.json_data = "[]"
            self.df = pd.DataFrame()

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