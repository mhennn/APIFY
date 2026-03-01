from core.get_data import GetData

class RequestData:
    def __init__(self):
        self.getData = GetData()

    def simple_data(self):
        return self.getData.get_simple_data()
    
    def key_value(self, key:str):
        try:
            if key:
                return self.getData.define_key(key)
            else:
                return {"detail": "No key provided"}
        except KeyError:
            return {"detail": f"{key} not found"}