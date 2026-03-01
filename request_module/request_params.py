from request_module.request_Data import RequestData

class RequestParam:
    def __init__(self, path="dataset/data.csv"):
        self.reqs_data = RequestData(path)

    def request_simple_data(self):
        return self.reqs_data.simple_data()
    
    def request_key_value(self, params=None):
        return self.reqs_data.key_value(params)