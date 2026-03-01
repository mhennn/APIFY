# APIFY-Go 🚀

APIFY-Go allows you to deploy custom Python scripts built with FastAPI, instantly turning your specific JSON datasets into live APIs. This approach provides a flexible, serverless backend that accelerates prototyping by letting you define complex data structures and endpoints directly in code.

---

### APIFY-Go features
- 💻 Built for speed, handles requests efficiently, making it ideal for serving data quickly in a cloud environment.
- 💻 You can easily integrate Apify's Dataset storage to save and retrieve your JSON dictionaries across different API requests.
- 💻 Handles API requests quickly and efficiently.
- 💻 Apify-go runs everything for you; you just focus on your code.
- 💻 Automatically creates a web page to test your API.
- 💻 Can be used as backend API for Flask

### Data Structural Application
```mermaid
graph LR
    A[git clone https://github.com/mhennn/APIFY-Go] --> B[Load your csv data on <br/>dataset/data.csv] --> C[Run the Program <br/> apiFy.py]
    C --> D(Initialize Class:<br/>RequestParam on your 'Main.py')
```

##### RequestParams has two(2) methods:
```bash
def request_simple_data(self):
    return self.reqs_data.simple_data()

>>> This can be used to get all the available data from your dataset
```
```bash
def request_key_value(self, params=None):
    return self.reqs_data.key_value(params)

>>> This can be used to get the value based on your set key
```

##### Testing the API

```bash
>>> test_file/test.py
from request_module.request_params import RequestParam

def test_all():
    reqs = RequestParam("./sample_dataset/data.csv")
    data = reqs.request_simple_data()
    return data

def test_key():
    reqs = RequestParam("./sample_dataset/data.csv")
    data = reqs.request_key_value("Role")
    return data

print(test_key())
print(test_all())

```
##### Output Test
```bash
['Developer', 'Strategist', 'Analyst', 'Designer']

[{'Employee': 1001, 'ID': 'Alice', 'Name': 'Johnson', 'Department': 'Engineering', 'Project': 'Lead', 'Role': 'Developer', 'Hours': 40, 'Worked': None}, {'Employee': 1002, 'ID': 'Bob', 'Name': 'Smith', 'Department': 'Marketing', 'Project': 'Content', 'Role': 'Strategist', 'Hours': 25, 'Worked': None}, {'Employee': 1003, 'ID': 'Charlie', 'Name': 'Davis', 'Department': 'Engineering', 'Project': 'QA', 'Role': 'Analyst', 'Hours': 35, 'Worked': None}, {'Employee': 1004, 'ID': 'Diana', 'Name': 'Evans', 'Department': 'Design', 'Project': 'UI', 'Role': 'Designer', 'Hours': 30, 'Worked': None}]
```