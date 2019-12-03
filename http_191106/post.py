# coding:utf-8
import requests
import requests.auth
import unittest
import random


class Test_job(unittest.TestCase):
    def setUp(self):
        s=str(random.randint(1,1000000))
        print("用例初始化开始")
        self.get_urls = "http://localhost:8080/jenkins/api/json?pretty=true"
        self.get_url = "http://localhost:8080/jenkins/job/check_python_version/api/json"
        self.copy_url="http://localhost:8080/jenkins/createItem?mode=copy&from=checkversion_python"\
                      +"&name=check_python_version"+random.choice("abcdefghijklmnopqrstuvwxyz")\
                      +s#保证名字不重复
        self.updata_url="http://localhost:8080/jenkins/job/check_python_version/description?description="+s
        self.build_url = "http://localhost:8080/jenkins/job/check_python_version/build"
        self.disable_url="http://localhost:8080/jenkins/job/check_python_version/disable"
        self.enable_url = "http://localhost:8080/jenkins/job/check_python_version/enable"
    def tearDown(self):
        print("用例清理完毕！")

    def test_get_all_jobs(self):
        print("###test_get_all_jobs......start###")
        status_code = requests.get(self.get_urls,data={},auth=("admin","cwx528938")).status_code
        self.assertEqual(200, status_code, u"获取所有job失败！")
        if status_code==200:
            print("获取所有job成功！")
        print("###test_get_all_jobs......end###")

    def test_get_job(self):
        print("###test_get_job.....start###")
        status_code=requests.get(self.get_url,data={},auth=("admin","cwx528938")).status_code
        self.assertEqual(200, status_code, u"获取job_code异常!")#断言出现中文要加u ,否则容易导致中文乱码
        if status_code==200:
            print("获取job成功！")
        else:
            print("获取job异常！")

        print("###test_get_job.....end!###")


    def test_copy_job(self):
        print("###test_copy_job....start###")
        status_code=requests.post(self.copy_url,data={},auth=("admin","cwx528938")).status_code
        self.assertEqual(200,status_code,u"复制job失败")
        if status_code==200:
            print("复制job成功")
        print("###test_copy_job....end!###")

    def test_updata_job(self):
        print("###test_updata_job....start###")
        status_code = requests.post(self.updata_url,data={},auth=("admin","cwx528938")).status_code
        self.assertEqual(204,status_code,"更新job失败！")
        if status_code==204:
            print("更新job成功！")
        print("###test_updata_job....end!###")

    def test_disable_enable_job(self):
        print("###test_disable_enable_job.......start###")
        status_1=requests.get(self.get_url, data={}, auth=("admin", "cwx528938")).json()["buildable"]#获取状态
        if status_1==False:
            print("this job has been disabled")
            requests.post(self.enable_url,data={},auth=("admin","cwx528938"))#发送启用请求
            status_3=requests.get(self.get_url, data={}, auth=("admin", "cwx528938")).json()["buildable"]  # 再次获取状态
            self.assertEqual(True,status_3,"启用失败！")#启用失败，断言失败
            if status_3==True:#断言成功，启用成功
                print("启用成功")
                requests.post(self.disable_url,data={},auth=("admin","cwx528938"))#启用成功后，发出禁用请求
                status_4 = requests.get(self.get_url, data={}, auth=("admin", "cwx528938")).json()[
                    "buildable"]  # 再次获取状态
                self.assertEqual(False,status_4,"禁用失败！")#禁用失败，断言失败
                if status_4==False:#断言成功，禁用成功
                    print("禁用成功！")

        elif status_1==True:
            print("this job has been enable")
            print("this job is  been disable")
            requests.post(self.disable_url,data={},auth=("admin","cwx528938"))#发送禁用请求
            status_2 = requests.get(self.get_url, data={}, auth=("admin", "cwx528938")).json()["buildable"]#再次获取状态
            self.assertEqual(False,status_2,"禁用失败!")#禁用失败，断言失败！
            if status_2==False:#断言成功，提示禁用成功
                print("禁用成功！")

        print("###test_disable_enable_job.......end###")



if __name__ == "__main__":
    unittest.main()