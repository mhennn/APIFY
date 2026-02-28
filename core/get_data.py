from utils.data import Data

class GetData:
    def __init__(self):
        self.data = Data()

    def get_simple_data(self):
        all_data = self.data.simple_data()
        return all_data
    
    def define_key(self, key_value):
        key_data = self.get_simple_data()[key_value]
        return key_data