# -*- encoding:utf-8 -*-
import unittest
import requests
import json
from parameterized import parameterized
from public.login import login
from public.deleletDealer import deleteDealer
from public.getData import getData



class dealerDealerNameCheck(unittest.TestCase):
    maxDiff = None


    def setUp(self):
        self.s = login()
        self.baseurl = "http://bhtest.51s.co/vc/system/dealer"
        self.dealerid = None


    successName = getData('dealerPostData.xlsx','dealer_dealername_success')
    @parameterized.expand(successName)
    def test_dealer_name_success(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['data']
        r = self.s.post(self.baseurl, json = datas)
        r.encoding = 'utf-8'
        result = r.json()
        resultData = result['data']
        self.dealerid = resultData['id']
        self.assertTrue(r.status_code, '200')
        self.assertEqual(resultData['name'], expectsData['name'])


    failName = getData('dealerPostData.xlsx','dealer_dealername_fail')
    @parameterized.expand(failName)
    def test_dealer_name_fail(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['error']
        r = self.s.post(self.baseurl, json=datas)
        r.encoding = 'utf-8'
        result = r.json()
        resultData = result['error']
        self.assertTrue(r.status_code, '200')
        self.assertEqual(resultData['code'], expectsData['code'])
        self.assertEqual(resultData['message'], expectsData['message'])

    successCode =  getData('dealerPostData.xlsx','dealer_code_success')
    def test_dealer_code_success(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['data']
        r = self.s.post(self.baseurl, json= datas)
        r.encoding = 'utf-8'
        result = r.json()
        resultData = result['data']
        self.dealerid = resultData['id']
        self.assertEqual(r.status_code, '200')
        self.assertEqual(resultData['code'], expectsData['code'])

    failCode = getData('dealerPostData.xlsx','dealer_code_fail')
    def test_dealer_code_fail(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['error']
        r = self.s.post(self.baseurl, json= datas)
        r.encoding = 'utf-8'
        result =  r.json()
        resultDatas = result['error']
        self.assertEqual(r.status_code, '200')
        self.assertEqual(resultDatas['code'], expectsData['code'])
        self.assertEqual(resultDatas['message'], expectsData['message'])

    successUsername = getData('dealerPostData.xlsx','dealer_username_success')
    def test_dealer_username_success(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['data']
        r = self.s.post(self.baseurl, json=datas)
        r.encoding('utf-8')
        result = r.json()
        resultData = result['data']
        self.dealerid = resultData['id']
        self.assertEqual(r.status_code, '200')
        self.assertEqual(resultData['userName'], expectsData['userName'])

    failUsername = getData('dealerPostData.xlsx','dealer_username_fail')
    def test_dealer_username_fail(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsResult = expects['error']
        r = self.s.post(self.baseurl, json= datas)
        r.encoding = 'utf-8'
        result = r.json()
        resultData = result['error']
        self.assertEqual(r.status_code, '200')
        self.assertEqual(resultData['code'], expectsResult['code'])
        self.assertEqual(resultData['message'], expectsResult['message'])

    successPassword = getData('dealerPostData.xlsx','dealer_password_success')
    def test_dealer_password_success(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['data']
        r = self.s.post(self.baseurl, json=datas)
        r.encoding = 'utf-8'
        result = r.json()
        resultData = result['data']
        self.dealerid = resultData['id']
        self.assertEqual(r.status_code, '200')
        self.assertEqual(resultData['password'],expectsData['password'])

    failPassword = getData('dealerPostData.xlsx','dealer_password_fail')
    def test_dealer_password_fail(self, _, data, expect):
        datas = eval(data)
        expects = eval(expect)
        expectsData = expects['error']
        r = self.s.post(self.baseurl, json= datas)
        r.encoding('utf-8')
        result = r.json()
        resultData = result['error']
        self.assertEqual(r.status_code, '200')
        self.assertEqual(resultData['code'], expectsData['code'])
        self.assertEqual(resultData['message'], expectsData['message'])





    def tearDown(self):
        deleteDealer(self.dealerid)
        if self.s:
            self.s.close()

    if __name__ == "__main__":
        unittest.main(verbosity=2)