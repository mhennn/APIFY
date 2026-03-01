from request_module.request_params import RequestParam

def test():
    reqs = RequestParam("sample_dataset/data.csv")
    data = reqs.request_key_value("Name")
    print(data)

test()