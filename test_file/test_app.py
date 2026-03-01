import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from request_module.request_Data import RequestData
from request_module.request_params import RequestParam
from core.get_data import GetData

class TestAPIFYGO_Functions(unittest.TestCase):
    def setUp(self):
        self.reqsParams = RequestParam()

    def test_simple_data(self):
        reqs_simple_data = self.reqsParams.request_simple_data()
        self.assertTrue(len(reqs_simple_data) > 0, "Path has no data")

    def test_key_value(self):
        reqs_key_value = self.reqsParams.request_key_value("Name")
        self.assertTrue(len(reqs_key_value) > 0, "Path has no data")

if __name__ == "__main__":
    unittest.main()