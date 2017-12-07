# -*- encoding:utf-8 -*-
import unittest
import json
from parameterized import parameterized
from public.login import login
from public.getData import getData
from public.deleletDealer import deleteDealer

class dealerAreaNameCheck(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.s = login()
        self.baseurl = "http://bhtest.51s.co/vc/system/dealer"
        self.dealerid = None

    successData = loadTestData("dealer_areaName_success.xlsx")
    @parameterized.expand(successData)
    def test_username_success(self, _, data, expect):
        datas = json.dumps(json.loads(data)).encode('utf-8')
        expects = eval(expect)
        r = self.s.post(self.baseurl, datas)
        result = r.json()
        self.dealerid = result['data']['id']
        result['data']['id'] = '1'
        result['data']['dealerAgentAreaList'][0]['dealerId'] = '1'
        result['data']['createdTime'] = 1509798757095
        self.assertEqual(result, expects)

    failData = loadTestData("dealer_areaName_fail.xlsx")
    @parameterized.expand(failData)
    def test_username_fail(self, _, data, expect):
        datas = json.dumps(json.loads(data)).encode('utf-8')
        expects = eval(expect)
        r = self.s.post(self.baseurl, datas)
        result = r.json()
        self.dealerid = ''
        self.assertEqual(result, expects)

    def tearDown(self):
        deleteDealer(self.dealerid)
        if self.s:
            self.s.close()


if __name__ == "__main__":
    unittest.main()
