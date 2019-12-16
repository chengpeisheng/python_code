########################################################################################################################
#自己写的提供本地测试的接口服务
########################################################################################################################
#coding:utf-8
from flask import Flask
from flask_restful import Api,request
import json

server=Flask(__name__)

@server.route("/login",methods=["post","get"])
def login():
    user_name=request.values.get("name")
    user_pwd=request.values.get("pwd")
    if user_name and user_pwd :
        if user_name=="xiaoming" and user_pwd=="111":
            result={"code":200,"message":"登录成功！"}
        elif user_name=="xiaoming" and user_pwd !="111":
            result={"code":401,"message":"用户名或密码错误！"}
        elif user_name != "xiaoming" and user_pwd == "111":
            result = {"code": 402, "message": "用户名或密码错误！"}
        elif user_name != "xiaoming" and user_pwd != "111":
            result = {"code": 403, "message": "用户名或密码错误！"}
    else:
        result = {"code": 404, "message": "用户名或密码不能为空！"}

    #如果要str格式结果，需要转化，也可以不用转化
    # result=json.dumps(result)
    # print(type(result))
    return result

if __name__=="__main__":
    server.run(host="127.0.0.1",port=8080,debug=True)