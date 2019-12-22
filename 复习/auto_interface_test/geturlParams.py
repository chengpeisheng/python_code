########################################################################################################################
#获取接口的URL、参数、method等
########################################################################################################################
from auto_interface_test import readConfig

readconfig=readConfig.ReadConfig()#构造读取配置对象

class geturlParams():#构造基本请求链接：http://127.0.0.1:8888/login?
    def get_url(self):
        new_url=readconfig.get_http("scheme")+"://"+readconfig.get_http("baseurl")+":8888"+"/login"+"?"
        return new_url

if __name__ == "__main__":
    print(geturlParams().get_url())