#coding:utf-8
#读取配置文件的方法，并返回文件中内容
import os
import configparser
import auto_test_frame.getpathInfo as getpathInfo#引入我们自己写的获取路径类
path = getpathInfo.get_Path()#调用这个方法
config_path=os.path.join(path,"config.ini")#将路径叠加，得出最终路径
config=configparser.ConfigParser()#python3中有这个包，读取外部文件的方法。构造对象config
config.read(config_path,encoding="utf-8")#调用对象config的read()方法读取配置文件的内容

class ReadConfig():
    def get_http(self,name):#读取http参数配置
        value=config.get("HTTP",name)
        return value
    def get_email(self,name):
        value=config.get("EMAIL",name)
        return value
    def get_mysql(self,name):
        value=config.get("DATABASE",name)
        return value

if __name__ == "__main__":
    print("HTTP中的baseurl值为：",ReadConfig().get_http("baseurl"))
    print("EMAIL 中的开关值on_off为：",ReadConfig().get_email("on_off"))
    print("DB_Type=",ReadConfig().get_mysql("DATA_TYPE"))




