# -*- encoding:utf-8 -*-
import unittest
import requests
import json
from parameterized import parameterized
from public.login import login
from public.loadTestData import loadTestData
from public.deleletDealer import deleteDealer



class dealerCompanyCheck(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.s = login()
        self.baseurl = "http://bhtest.51s.co/vc/system/dealer"
        self.dealerid = None

    testData = loadTestData("dealer_company.xlsx")
    @parameterized.expand(testData)
    def test_company_check_normal(self, _, data, expect):
        datas = json.dumps(json.loads(data)).encode('utf-8')
        expects = eval(expect)
        r = self.s.post(self.baseurl, datas)
        result = r.json()
        self.dealerid = result['data']['id']
        result['data']['id'] = '1'
        result['data']['dealerAgentAreaList'][0]['dealerId'] = '1'
        result['data']['createdTime'] = 1509798757095
        self.assertEqual(result, expects)

    def tearDown(self):
        deleteDealer(self.dealerid)
        if self.s:
            self.s.close()


    if __name__ == "__main__":
        unittest.main(verbosity=2)
