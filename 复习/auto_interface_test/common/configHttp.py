########################################################################################################################
#这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应。
########################################################################################################################
import requests
import json

class RunMain():
    def send_post(self,url,data,header=None):
        res=requests.post(url=url,data=data).json()
        return res


    def send_get(self,url,data,header=None):
        res=requests.get(url=url,data=data).json()
        print(res)
        return res

    def run_main(self,method=None,url=None,data=None):
        result=None
        if method == "post":
            result=self.send_post(url,data)
        elif method=="get":
            result=self.send_get(url,data)
        else:
            print("method值错误！！！")
        return result


if __name__ == "__main__":
    RunMain().run_main(method="get",url="http://127.0.0.1:8080/login?pwd=111&name=xiaoming")
    RunMain().run_main(method="post", url="http://127.0.0.1:8080/login?pwd=111&name=xiaoming")

