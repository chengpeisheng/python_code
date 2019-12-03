#coding:utf-8
#print u"中文"#print函数:中文前带有u,文字变成草绿色，没有则变成黄绿色,2者都可以
import requests
import unittest
import json

class TestBlog(unittest.TestCase):
    def setUp(self):
        #全局变量配置表，方便后续用例进行调用
        self.get_all_blogs_url="http://localhost:12306/get_all_posts"
        self.get_a_comment_url="http://localhost:12306/get_a_comment"
        self.create_blog_url="http://localhost:12306/create_a_blog"
        self.edit_blog_url="http://localhost:12306/edit_first_blog/2"
        self.delete_blog_url="http://localhost:12306/delete_first_blog/1"

        self.headers = {"Content-Type": "application/json"}
        print(u"###用例初始结束###")
    def tearDown(self):
        print(u"###用例执行结束结束###")
    def test_get_all_blogs(self):
        result_01_code=requests.get(self.get_all_blogs_url,data={}).status_code#①因为是mock的不需要auth=("xxx","xx")；
        result_01 = requests.get(self.get_all_blogs_url, data={}).json()
        self.assertEqual(200,result_01_code,u"①获取所有blogs失败")#断言提示语必须加u,否则中文报乱码
        self.assertEqual("/get_all_posts",result_01[0]["url"],u"②获取所有blogs失败")#断言提示语必须加u,否则中文报乱码
        self.assertEqual("/get_one_post", result_01[1]["url"], u"③获取所有blogs失败")  # 断言提示语必须加u,否则中文报乱码
        self.assertEqual(2,len(result_01),u"④获取所有blogs失败")#返回的结果是列表，一定要判断长度


    def test_get_a_comment(self):
        result_01_code=requests.get(self.get_a_comment_url).status_code
        result_01=requests.get(self.get_a_comment_url,data={}).json()
        self.assertEqual(200,result_01_code,U"①获取评论失败")#content==str,json()==dict,text==unicode
        self.assertEqual("chengpeisheng",result_01["author"],u"②获取评论失败")
        self.assertEqual("this is my first blog!",result_01["comment"],u"③获取评论失败")

    def test_create_blog(self):
        json_data=json.dumps({"title":"food","comment":"milk is very teasty!"})
        result=requests.post(self.create_blog_url,data=json_data,headers=self.headers)
        self.assertEqual(200,result.status_code,u"创建blog成功")
        self.assertEqual("success",result.json()["result"],u"获取blog成功")



    def test_edit_blog(self):
        json_data=json.dumps({"title":"food","comment":"milk is very teasty!"})#将字典转化为json格式的字符串
        result=requests.put(self.edit_blog_url,data=json_data,headers=self.headers)#url:字符串，data:字符串，headers:字典
        self.assertEqual(200,result.status_code,u"编辑blog失败")
        self.assertEqual("success",result.json()["result"],u"编辑blog失败")

    def test_delete_blog(self):
        result=requests.delete(self.delete_blog_url)#返回结果
        self.assertEqual(200,result.status_code,u"删除blog成功！")
        self.assertEqual("success",result.json()["result"],u"删除blog成功！")#将json结果转化为字典进行断言


if __name__ == "__main__":
    unittest.main()