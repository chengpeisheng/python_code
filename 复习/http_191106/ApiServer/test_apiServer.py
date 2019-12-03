#coding:utf-8
#测试对象：用peewee和flask写的接口
#测试接口如下
#get /posts/<post_id> 获取某个博客接口数据
#put /posts/<post_id>   修改某个博客接口数据
#delete /posts/<post_id>    删除某个博客接口数据
#get /posts 获取所有博客接口数据
#post /posts    创建一个博客接口数据

import unittest
import requests
import json
import random
from flask import g,Flask

#定义Flask框架，Api框架
app=Flask(__name__)

#引入model
from peewee import *

db=SqliteDatabase("post.db")

class Post(Model):
    title=CharField(unique=True)
    content=TextField()
    class Meta():
        database=db

@app.before_request
def before_request():
    g.db=db
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response



class Test_Blogs(unittest.TestCase):
    def setUp(self):
        self.url_get_all_blogs="http://127.0.0.1:5000/posts"
        self.url_post_a_blog="http://127.0.0.1:5000/posts"
        self.header={"Content-Type":"application/json"}
        print("预置数据准备完毕！")


    def tearDown(self):
        print("脏数据清理完毕！")

    def test_get_a_blog(self):
        # 数据准备：创建blog,并获取uri供其他接口使用
        data_dict1 = {
            "title": "title" + str(random.randint(0, 999999)),
            "content": "content" + str(random.randint(0, 999999))
        }
        title_1=data_dict1["title"]#写入数据库title
        data_json1 = json.dumps(data_dict1)#发送数据前要转化为json格式字符串
        response1 = requests.post(url=self.url_post_a_blog, headers=self.header, data=data_json1, auth=None)
        uri_1 = response1.json()["uri"]#json格式的response转化为dict格式，并取出uri

        #查询数据库是否有创建的数据
        data3 = Post.get(Post.title == title_1)#从数据库中查找写入的title,并返回，然后做对比
        title_2=data3.title
        self.assertEqual(title_2,title_1,"数据没写入数据")#判断写入的数据和查询到的数据是否一致
        self.assertEqual(200, response1.status_code, "状态码错误！")#判断数据写入后响应码是否正确



        #测试环节：获取创建的blog
        response2=requests.get(url=uri_1,headers=self.header,data=None,auth=None)
        self.assertEqual(200,response2.status_code,"test_get_a_blog:状态码错误！")

        #数据清理：删除创建的blog
        response3=requests.delete(url=uri_1,headers=self.header,data=None,auth=None)
        try:
            Post.get(Post.title == title_1)  # 判断数据库是否存在已经删除的title,不存在则抛异常：Post.DoesNotExist
        except Post.DoesNotExist :#删除成功了在判断状态码是否正确
            self.assertEqual(200, response3.status_code, "状态码错误！")
            # 返回获取的blog
            return response2.json()

    def test_put_a_blog(self):
        #数据准备：创建blog,并获取uri供其他接口使用
        data_dict1 = {
            "title": "title" + str(random.randint(0, 999999)),
            "content": "content" + str(random.randint(0, 999999))
        }
        title_1=data_dict1["title"]#写入数据库的title
        data_json1 = json.dumps(data_dict1)
        response1 = requests.post(url=self.url_post_a_blog, headers=self.header, data=data_json1, auth=None)
        try:
            Post.get(Post.title == title_1)  # 判断数据是否写入数据库
        except Post.DoesNotExist:
            return "数据创建失败，数据准备失败！"
        self.assertEqual(200, response1.status_code, "状态码错误！")#如果数据写入，再判断状态码对不对
        uri_1 = response1.json()["uri"]


        #测试环节：修改blog
        data_dict2 = {
            "title": "title" + str(random.randint(0, 999999)),
            "content": "content" + str(random.randint(0, 999999))
        }
        title_2=data_dict2["title"]#修改的title
        data_json2=json.dumps(data_dict2)
        response2=requests.put(url=uri_1,headers=self.header,data=data_json2,auth=None)#要指明数据类型为json字符串，否则报500
        try:
            Post.get(Post.title == title_2)#数据修改后及时查询数据库，看是否有这个title，有则判断code对不对
        except Post.DoesNotExist:
            return "数据修改失败！"
        self.assertEqual(200,response2.status_code,"test_put_a_blog:状态码错误！")

        #数据清理：删除创建的blog
        response3= requests.delete(url=uri_1, headers=self.header, data=None, auth=None)
        try:
            Post.get(Post.title == title_2)#数据删除后及时查询数据库，看是否有这个title，没则判断code对不对
        except Post.DoesNotExist:
            self.assertEqual(200, response3.status_code, "test_del_a_blog:状态码错误！")
        return response2.json()


    def test_del_a_blog(self):
        # 数据准备：创建blog,并获取uri供其他接口使用
        data_dict1 = {
            "title": "title" + str(random.randint(0, 999999)),
            "content": "content" + str(random.randint(0, 999999))
        }
        data_json1 = json.dumps(data_dict1)
        title_1=data_dict1["title"]
        response1 = requests.post(url=self.url_post_a_blog, headers=self.header, data=data_json1, auth=None)
        try:#判断创建的数据是否存在
            Post.get(Post.title==title_1)
        except Post.DoesNotExist:
            return "数据创建失败，数据准备失败！"
        self.assertEqual(200,response1.status_code,"状态码错误")#如果数据库中存在创建的数据，再判断返回码
        uri_1 = response1.json()["uri"]


        # 测试环节：删除创建的blog
        response2 = requests.delete(url=uri_1, headers=self.header, data=None, auth=None)
        self.assertEqual(200, response2.status_code, "test_del_a_blog:状态码错误！")
        try:#判断删除的数据是否存在
            Post.get(Post.title==title_1)
        except Post.DoesNotExist:
            return response2.json()
        return "删除成功！"




if __name__=="__main__":
    unittest.main()




