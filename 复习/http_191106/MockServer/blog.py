###############################
#1.测试获取所有文章接口
#2.测试获取某篇文章的接口
###############################
import unittest
import requests
import json

class TestBlog(unittest.TestCase):
    def setUp(self):
        self.url_get_all_blogs="http://localhost:12306/posts"
        self.url_get_a_blog="http://localhost:12306/posts/3"
        self.url_create_blog="http://localhost:12306/posts"
        self.url_edit_a_blog="http://localhost:12306/posts/2"
        self.url_delete_a_blog = "http://localhost:12306/posts/1"
        print("用例初始化完毕！")
    def tearDown(self):
        print("脏数据清理完毕！")
    def test_get_all_blogs(self):
        response=requests.get(url=self.url_get_all_blogs,data={},auth=("cwx528938","528938"))
        self.assertEqual(200,response.status_code,"获取所有blog失败")
        self.assertEqual("first post",response.json()[0]["title"],"title 异常")
        self.assertEqual("/posts/1",response.json()[0]["uri"],"uri 异常")
        self.assertEqual("second post",response.json()[1]["title"], "title 异常")
        self.assertEqual("/posts/2", response.json()[1]["uri"], "uri 异常")


    def test_get_a_blog(self):
        response = requests.get(url=self.url_get_a_blog, data={}, auth=("cwx528938", "528938"))
        self.assertEqual(200, response.status_code, "获取blog失败")
        self.assertEqual("third post", response.json()["title"], "title 异常")
        self.assertEqual("/posts/3", response.json()["uri"], "uri 异常")

    def test_create_blog(self):
        headers = {"Content-Type": "application/json"}#发送有body的请求要有headers, 规定好body是什么类型数据，不写的话系统默认是json类型
        request = {"title": "food", "comment": "milk is very teasty!"}
        request=json.dumps(request)
        response=requests.post(url=self.url_create_blog,headers=headers,data=request,auth=("cwx528938","528938"))
        self.assertEqual(200,response.status_code,"创建blog失败！")
        self.assertEqual(True,response.json())

    def test_edit_a_blog(self):
        headers = {"Content-Type": "application/json"}  # 发送有body的请求要有headers, 规定好body是什么类型数据，不写的话系统默认是json类型
        request = { "title": "first post has been fixed", "uri": "/posts/2"}
        request = json.dumps(request)
        response = requests.put(url=self.url_edit_a_blog, headers=headers, data=request, auth=("cwx528938", "528938"))
        self.assertEqual(400,response.status_code,"编辑blog失败")

    def test_delete_a_blog(self):
        headers={"Content-Type":"application/json"}#没有请求体，可以不写
        response=requests.delete(url=self.url_delete_a_blog,headers=headers,data=None,auth=("cwx528938","528938"))
        self.assertEqual(200,response.status_code,"删除失败，返回码异常！")
        self.assertEqual("delete success !", response.text, "删除失败，返回码异常！")


if __name__ == "__main__":
    unittest.main()
