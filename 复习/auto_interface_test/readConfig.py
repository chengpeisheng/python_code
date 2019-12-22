########################################################################################################################
#读取配置文件的方法，并返回文件中内容
########################################################################################################################
#coding:utf-8
import os
import configparser
from auto_interface_test import getpathInfo

path=getpathInfo.get_Path()#调用获取项目文件绝对路径的方法
config_path=os.path.join(path,"config.ini")#获取config.ini的绝对路径
config=configparser.ConfigParser()#生成config对象，用于解析配置
config.read(config_path,encoding="utf-8")#读取config.ini配置

class ReadConfig():
    def get_http(self,name):
        value=config.get("HTTP",name)#获取section下面option的值
        return value
    def get_email(self,name):
        value=config.get("EMAIL",name)#获取section下面option的值
        return value
    def get_mysql(self,name):
        value=config.get("DATABASE",name)#获取section下面option的值
        return value

if __name__ == "__main__":
    print("HTTP中baseurl的值为：",ReadConfig().get_http(name="baseurl"))
    print("EMAIL中的开关on_off值为：", ReadConfig().get_email(name="on_off"))


