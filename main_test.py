import sys, time
#sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText

test_dir='F:\\Projects\\bhAPItest\\bhAPItest\\testcases1'
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#发送邮件
def sentmail(filename):
    file_new=filename
    #发信邮箱
    mail_from='pms@erathink.com'
    #收信邮箱
    mail_to=['qtang@erathink.com']
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"万码易联测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.qiye.163.com')
    #用户名密码
    smtp.login('pms@erathink.com','Pms20152015')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print ('email has send out !')

if __name__=="__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='F:\\Projects\\bhAPItest\\bhAPItest\\report\\'+now+'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='bhAPItest',description='test')
    runner.run(discover)
    fp.close()
    sentmail(filename)
    
