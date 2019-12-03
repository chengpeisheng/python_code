#coding:utf-8
################################################################################
#利用python 向jenkins发送get请求
#date:2019-9-28
#editor:chengpeisheng
#lastest_edit:2019-9-28
################################################################################
#方法一：py2中运行此代码，py3中没有httplib模块，替代模块是requests
# import httplib#py3中无此模块，
# http_client = httplib.HTTPConnection("localhost",8080,timeout=30)
# http_client.request("Get","/jenkins/api/json?pretty=true")
# reponse = http_client.getresponse()
# # print reponse.read()
# # print reponse.status
# print(reponse.read())
# print(reponse.status)




#方法二:py2中运行此代码，py3中没有urllib2模块，替代模块是requests
# import urllib2#py3中取消了此模块，替代模块是requests
# response = urllib2.urlopen("http://localhost:8080/jenkins/api/json?pretty=true")
# print(response.read())


################################################################################
#利用python 向jenkins发送post请求,不带鉴权模式
#date:2019-9-28
#editor:chengpeisheng
#lastest_edit:2019-9-28
#py2中运行此代码，py3中没有urllib2模块，替代模块是requests
###############################################################################
# import urllib2
# import urllib
# post_data = urllib.urlencode({})
# response = urllib2.urlopen("http://localhost:8080/jenkins/job/check_python_version/polling",post_data)
# print response.read()


################################################################################
#利用python 向jenkins发送post请求,带鉴权模式
#date:2019-9-28
#editor:chengpeisheng
#lastest_edit:2019-9-28
#运行环境：python 3.7
###############################################################################
#方法1，导入HTTPBasicAuth类,在py3.7运行
# import requests
# from requests.auth import HTTPBasicAuth
# url = "http://localhost:8080/jenkins/job/check_python_version/disable"
# result=requests.post(url=url,auth=HTTPBasicAuth("admin","cwx528938"))
# print(result.status_code)
# print(result.headers)
# print(result.reason)

#方法2，不导入HTTPBasicAuth类，直接简写auth=("UserCount","UserPassword"),默认是用户名在前密码在后，不可反过来
#运行环境：py37
# import requests
# url="http://localhost:8080/jenkins/job/check_python_version/disable"
# result=requests.post(url=url,data=None,auth=("admin","cwx528938"))
# print(result.status_code)
# print(result.headers)
