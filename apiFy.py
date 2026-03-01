from fastapi import FastAPI
from request_module.request_params import RequestParam

app = FastAPI(debug=True)
reqParams = RequestParam()

def path():
    data_path = "sample_dataset/data.csv"
    return data_path

@app.get('/')
def home():
    return {
        "Message": "Welcome to APIFY",
        "Available Route": [
            "/simpleData",
            "/keyValue"
            ]
        }

@app.get('/simpleData')
def simple_data():
    return reqParams.request_simple_data()

@app.get('/keyValue/')
def key_value():
    return reqParams.request_key_value()