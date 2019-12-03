#coding:utf-8
#这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应。
import requests
import json

class RunMain():
    def send_post(self,url,data):#定义一个post方法，传入url,data，给用户返回字典和字符串格式的结果
        result = requests.post(url=url,data=data).json()#发送post请求，并将得到的数据转化为dict
        res=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)#将字典序列化为字符串
        #上面两部有点多余，直接将用requests.post(xx).content 就可以把字符串结果返回过来
        return result

    def send_get(self,url,data):#定义一个get方法，传入url,data，给用户返回字典和字符串格式的结果
        result = requests.get(url=url,data=data).json()#data形式可以是字段，字符串
        res=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        # 上面两部有点多余，直接将用requests.get(xx).content 就可以把字符串结果返回过来
        return res
    def run_main(self,method,url=None,data=None):#请求的data只能是dict不能是string
        result=None
        if method=="post":
            result=self.send_post(url,data)

        elif method=="get":
            result=self.send_get(url,data)
        else:
            print("method 值错误！！！")
        return result

if __name__ == "__main__":#通过写死参数，来验证我们写的请求是否正确
    resutl_1 = RunMain().run_main("post","http://127.0.0.1:8888/login",{"name":"xiaoming","pwd":"111"})
    resutl_2 = RunMain().run_main("post","http://127.0.0.1:8888/login","name=xiaoming&pwd=111")
    print(resutl_1)
    print(resutl_2)