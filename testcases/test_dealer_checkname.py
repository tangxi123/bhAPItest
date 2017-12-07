# -*- encoding:utf-8 -*-
import unittest
import requests
import json
from parameterized import parameterized
from public.login import login
from public.loadTestData import loadTestData



class dealerCheckName(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(self):
        self.s = login()
        self.baseurl_checkname = "http://bhtest.51s.co/vc/system/dealer/checkname"

    value_notExist = json.dumps({"property": "name", "value": "一级经销商2"}).encode('utf-8')
    value_notExist_expect = {'error':None,'data':True}
    value_exist = json.dumps({"property": "name", "value": "一级经销商汤"}).encode('utf-8')
    value_exist_expect = {'error':None,'data':False}
    value_isNull = json.dumps({"property": "name", "value": ""}).encode('utf-8')
    value_isNull_expect = {'data': None, 'error': {'code': 'COMM_PARAM_EMPTY', 'message': '用户名不允许为空'}}
    value_isSpaces = json.dumps({"property": "name", "value": ""}).encode('utf-8')
    value_isSpaces_expect = {'data': None, 'error': {'code': 'COMM_PARAM_EMPTY', 'message': '用户名不允许为空'}}
    value_hasSpaces = json.dumps({"property": "name", "value": " 经销商有空格 "}).encode('utf-8')
    value_hasSpaces_expect = {'error':None,'data':True}
    property_notName = json.dumps({"property": "hello", "value": "一级经销商2"}).encode('utf-8')
    property_notName_expect = {'data': None, 'error': {'code': 'COMM_PARAM_EMPTY', 'message': '用户名不允许为空'}}
    property_isNull = json.dumps({"property": "", "value": "一级经销商2"}).encode('utf-8')
    property_isNull_expect = {'data': None, 'error': {'code': 'COMM_PARAM_EMPTY', 'message': '用户名不允许为空'}}
    property_isSpaces = json.dumps({"property": "   ", "value": "一级经销商2"}).encode('utf-8')
    property_isSpaces_expect = {'data': None, 'error': {'code': 'COMM_PARAM_EMPTY', 'message': '用户名不允许为空'}}
    property_hasSpaces = json.dumps({"property": "  name  ", "value": "一级经销商2"}).encode('utf-8')
    property_hasSpaces_expect = {'data': None, 'error': {'code': 'COMM_PARAM_EMPTY', 'message': '用户名不允许为空'}}


    # @parameterized.expand([
    #     ("value_notExist", value_notExist, value_notExist_expect),
    #     ("value_exist", value_exist, value_exist_expect),
    #     ("value_isNull", value_isNull, value_isNull_expect),
    #     ("value_isSpaces", value_isSpaces, value_isSpaces_expect),
    #     ("value_hasSpaces", value_hasSpaces, value_hasSpaces_expect),
    #     ("property_notName", property_notName, property_notName_expect),
    #     ("property_isNull", property_isNull, property_isNull_expect),
    #     ("property_hasSpaces", property_hasSpaces, property_hasSpaces_expect)
    # ])
    testData = loadTestData("checkname.xlsx")
    @parameterized.expand(testData)
    def test_checkname(self, _, data, expect):
        datas = json.dumps(json.loads(data)).encode('utf-8')
        expects = eval(expect)
        r = self.s.post(self.baseurl_checkname, datas)
        result = r.json()
        self.assertEqual(result, expects)

    @classmethod
    def tearDownClass(self):
        self.s.get('http://bhtest.51s.co/signin')



if __name__ == "__main__":
    unittest.main(verbosity=2)
