#coding:utf-8
#读取userCase.xlsx中的用例，使用unittest来进行断言校验
from auto_test_frame.geturlParams import  Geturl_Params
from auto_test_frame.readExcel import ReadExcel
import unittest
import requests
import warnings

url=Geturl_Params().get_Url()#获取url前半部分
login_xls=ReadExcel().get_xls("userCase.xlsx" ,"login")#读取用例表格

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)

        pass
    def tearDown(self):
        pass
    def test_01_Login(self):
        print("测试用例1：正常登陆，账号和密码都正确")
        url1=url+login_xls[0][2]#login_xls[行号][列号]
        dict_result=requests.post(url=url1,data=None,auth=None).json()
        self.assertEqual(200,dict_result["code"],u"用例失败")
        self.assertEqual("登录成功",dict_result["message"],u"message提示语不符合标准")

    def test_02_Login(self):
        print("测试用例2：密码错误")
        url1=url+login_xls[1][2]#login_xls[行号][列号]
        dict_result=requests.post(url=url1,data=None,auth=None).json()
        self.assertEqual(-1,dict_result["code"],u"用例失败")
        self.assertEqual("账号密码错误",dict_result["message"],u"message提示语不符合标准",)

    def test_03_Login(self):
        print("测试用例3：密码为空")
        url1 = url + login_xls[2][2]  # login_xls[行号][列号]
        dict_result = requests.post(url=url1, data=None, auth=None).json()
        self.assertEqual(10001, dict_result["code"], u"用例失败")
        self.assertEqual("参数不能为空", dict_result["message"], u"message提示语不符合标准", )
    # def test_Send_Email(self):
    #     # configEmail.Send_Email().send_QQ_Email()#直接使用类调用方法来发送邮件，下面的方法更标准，本方法更简单
    #     send_email = Send_Email()  # 构造发送邮件对象
    #     send_email.send_QQ_Email()  # 通过send_email对象调用send_QQ_Email()方法
    #     print("Email has send over!")
if __name__ == "__main__":
    unittest.main()





