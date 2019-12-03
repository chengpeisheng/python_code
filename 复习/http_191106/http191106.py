import  unittest
import requests
import random

class TestJenkins(unittest.TestCase):
    def setUp(self):
        self.get_jobs_url="http://localhost:8080/jenkins/api/json?pretty=true"
        self.get_job_url="http://localhost:8080/jenkins/job/check_python_version/api/json"
        self.copy_job_url = "http://localhost:8080/jenkins/createItem?name=check_python_version_%s&mode=copy&from=check_python_version"%random.randint(1,9999999)
        self.check_python_version_url = "http://localhost:8080/jenkins/job/check_python_version/polling"
        self.update_job_description_url = "http://localhost:8080/jenkins/job/check_python_version/description?description=100555"
        self.perform_job_url = "http://localhost:8080/jenkins/job/check_python_version/build"
        self.disable_job_url = "http://localhost:8080/jenkins/job/check_python_version/disable"
        self.enable_job_url = "http://localhost:8080/jenkins/job/check_python_version/enable"
        print("数据初始化完毕")
    def tearDown(self):
        print("数据清理完毕")

    def test_get_jobs(self):
        response=requests.get(url=self.get_jobs_url,auth=("admin","cwx528938"))
        self.assertEqual(200,response.status_code,"test_get_jobs---fail!")
        self.assertEqual("NORMAL",response.json()["mode"],"test_get_jobs---fail!")
        self.assertEqual("the master Jenkins node", response.json()["nodeDescription"], "test_get_jobs---fail!")
        self.assertEqual("check_python_version", response.json()["jobs"][0]["name"], "test_get_jobs---fail!")#找到jobs的第0个name

    def test_copy_job(self):
        response=requests.post(url=self.copy_job_url,data={},auth=("admin","cwx528938"))
        self.assertEqual(200,response.status_code,"test_copy_job---fail!")

    def test_check_python_version(self):
        response = requests.post(url=self.copy_job_url, data={}, auth=("admin", "cwx528938"))
        self.assertEqual(200, response.status_code, "test_check_python_version---fail!")

    def test_update_job_description(self):
        response=requests.post(url=self.update_job_description_url,data={}, auth=("admin", "cwx528938"))
        self.assertEqual(204, response.status_code, "test_update_job_description---fail!")

    def test_perform_job(self):
        response = requests.post(url=self.perform_job_url, data={}, auth=("admin", "cwx528938"))
        self.assertEqual(201, response.status_code, "test_perform_job---fail!")

    def test_disable_job(self):
        response1=requests.get(url=self.get_job_url, auth=("admin", "cwx528938"))
        if response1.json()["buildable"]==True:#job是开启状态，直接下发禁用请求
            response = requests.post(url=self.disable_job_url, data={}, auth=("admin", "cwx528938"))
            self.assertEqual(200, response.status_code, "test_disable_job---fail!")
        else:#job是禁用状态，要先下发启用请求，再下发禁用请求
            self.test_enable_job()
            response = requests.post(url=self.disable_job_url, data={}, auth=("admin", "cwx528938"))
            self.assertEqual(200, response.status_code, "test_disable_job---fail!")

    def test_enable_job(self):
        response1 = requests.get(url=self.get_job_url, auth=("admin", "cwx528938"))#先获取job状态
        if response1.json()["buildable"] == False:  # job是禁用状态，直接下发启用请求
            response = requests.post(url=self.enable_job_url, data={}, auth=("admin", "cwx528938"))
            self.assertEqual(200, response.status_code, "test_enable_job---fail!")
        else: # job是启用用状态，先下发禁用请求，再下发启用请求
            self.test_disable_job()
            response=requests.post(url=self.enable_job_url,data={},auth=("admin","cwx528938"))
            self.assertEqual(200,response.status_code,"test_enable_job fail!")

if __name__=="__main__":
    unittest.main()

