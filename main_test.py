import sys, time
#sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest

test_dir='E:\\projects\\bhAPItest\\testcases'
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__=="__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='E:\\projects\\bhAPItest\\report\\'+now+'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='bhAPItest',description='test')
    runner.run(discover)
    fp.close()
    
