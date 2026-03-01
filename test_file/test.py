import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from request_module.request_params import RequestParam

def test_all():
    reqs = RequestParam("./sample_dataset/data.csv")
    data = reqs.request_key_value("Name")
    return data

def test_key():
    reqs = RequestParam("./sample_dataset/data.csv")
    data = reqs.request_key_value("Email")
    return data

print(test_key())
print(test_all())