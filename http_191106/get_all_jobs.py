#coding:utf-8
#序列化---json.dumps()和反序列化----json.loads()
# import json
# # 将python 的dict转化为json的dict 叫序列化，用json.dumps(python_dict)
# # 将json 的dict转化为python的dict 叫反序列化，用json.loads(json_dict)
# python_dict={"a":"apple","b":"banana"}#python的字典
# print python_dict
# json_dict=json.dumps(python_dict)#序列化
# python_dict2 = json.loads(json_dict)
# print "json_dict"
# print json_dict
# print "python_dict2"
# print python_dict2


#需求：向jenkins发起请求，获取所有job,并判断获取的第1个job的name是否等于“chenk_python_version”
#方法一：使用json.loads()函数反序列化
# import unittest
# import json
# import requests
# import requests.auth#导入auth模块，只要是使用里面的HTTPBasicAuth
# #from requests.auth import HTTPBasicAuth#作用同上，导入了具体使用的HTTPBasicAuth类
# class Test_get_all_jobs(unittest.TestCase):#所有测试类必须继承unittest.TestCase类
#     def setUp(self):#只有继承了unitest.TestCase类有才可以调用其内部setUp方法
#         self.r=requests.get("http://localhost:8080/jenkins/api/json?pretty=true",auth=("admin","cwx528938"))
#         print "用例初始化完毕"
#
#     def tearDown(self):#数据清理部分放在这个部分
#         print "用例数据清理完毕"
#
#     def test_get_all_jobs(self):
#         json_dict = self.r.text#json_dict格式文本
#        #json_dict = self.r.text  # 同上也是json_dict格式文本
#         print "#####json_dict#####"
#         print json_dict
#         python_dict =json.loads(json_dict)#将json_dict格式文本反序列化成python_dict,只有python_dict支持使用dict[key]方式访问
#         print "#####python_dict#####"
#         print python_dict
#         self.assertEqual(python_dict["jobs"][0]["name"],"check_python_version")#通过对python_dict的访问来断言
#
# if __name__ == "__main__":
#     unittest.main()


# #方法二：直接使用requests模块，将获取的json_dict信息转化为python_dict
import unittest
import requests
import requests.auth #导入模块auth,开启鉴权模式
import http.client
#from requests.auth import HTTPBasicAuth#作用同上，导入了具体使用的基本鉴权类
# class Test_get_all_jobs(unittest.TestCase):#所有测试类必须继承unittest.TestCase类
#     def setUp(self):#只有继承了unitest.TestCase类有才可以调用其内部setUp方法
#         self.r=requests.get("http://localhost:8080/jenkins/api/json?pretty=true",auth=("admin","cwx528938"))
#         print("用例初始化完毕")
#
#     def tearDown(self):#数据清理部分放在这个部分
#         print("用例数据清理完毕")
#
#     def test_get_all_jobs(self):
#         print(" ##self.r.text##")
#         print(self.r.text)  #text和content都是json_dict格式
#         print(" ##self.r.content##")
#         print(self.r.content) #text和content都是json_dict格式
#         python_dict = self.r.json()#将json_dict反序列化为python_dict
#         print("####python_dict######")
#         print(python_dict)
#         self.assertEqual(python_dict["jobs"][0]["name"],"check_python_version")
#         self.assertEqual(python_dict["jobs"][-1]["name"], "checkversion_python")
#
# if __name__ == "__main__":
#     unittest.main()
#
#


###########################复习时候练习################################




#coding=utf-8
import requests
import unittest
import json


class Get_all_jobs(unittest.TestCase):
    def setUp(self):
        #变量前加self,可以被类中所有方法调用 ，调用时加self
        self.get_all_jobs_url="http://localhost:8080/jenkins/api/json?pretty=true"
        print("用例初始化完毕")

    def tearDown(self):
        print("用例数据清理完毕")
    def test_GetAllJobs(self):
        response=requests.get(url=self.get_all_jobs_url,data={},auth=None)
        response_dict=response.json()#将str->dict
        self.assertEqual(200,response.status_code,"获取所有jobs失败")
        self.assertEqual("check_python_version",response_dict["jobs"][0]["name"],"名称不符合")
if __name__=="__main__":
    unittest.main()




















