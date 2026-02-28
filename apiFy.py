from fastapi import FastAPI
from core.get_data import GetData

app = FastAPI(debug=True)
getData = GetData()
key_param = "username" # Change the "username" as the parameter

@app.get('/simpleData')
def simple_data():
    return getData.get_simple_data()

@app.get('/keyValue/')
def key_value(key:str = key_param):
    return getData.define_key(key)