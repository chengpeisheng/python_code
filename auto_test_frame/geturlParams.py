#coding:utf-8
#获取接口的URL、参数、method等
from auto_test_frame.readConfig import ReadConfig

class Geturl_Params():
    def get_Url(self):
        new_url=ReadConfig.get_http(self,"scheme")+"://"+ReadConfig.get_http(self,"baseurl")+":8888/login"+"?"
        return new_url

if __name__ == "__main__":
    print(Geturl_Params().get_Url())




