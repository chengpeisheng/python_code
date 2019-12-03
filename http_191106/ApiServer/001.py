#coding:utf-8
from flask import Flask,request,g
from flask_restful import reqparse,abort,Api,Resource

#创建一个app服务，并生成对应api接口框架
app = Flask(__name__)#定义一个app对象
api=Api(app)#给app生成对应的接口api
app.debug=True

#引进model
from peewee import *
db=SqliteDatabase("posts.db")#创建一个数据库posts.db

class Post(Model):#创建一个Post表，这个表继承了Model类的所特性，
    title=CharField(unique=True)#创建一个char类型的title字段，并且是唯一的
    content=TextField()#创建一个text类型的content字段
    class Meta:#内嵌一个Meta类
        database=db

#定义一个列表
# POSTS=[
#     {},
#     {"title":"first post","content":"first post"},
#     {"title":"second post","content":"second post"},
#     {"title":"third post","content":"third  post"}
# ]


"""
定义自动连接数据库和关闭数据库
"""
@app.before_request
def before_request():
    g.db=db
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

#对每个post_id进行判断是否异常,异常则退出，报错
def abort_if_postnt_exist(post_id):
    """
    上面被注释的代码是对程序中的列表进行操作，现在要修改逻辑，要对数据库的数据进行操作

    """
    post_id=int(post_id)
    try:
        Post.get(Post.id==post_id)
    except Post.DoesNotExist:
        abort(404 ,message="POSTS doesn~t exist")

parser=reqparse.RequestParser()#构造请求解析器
parser.add_argument("get",type=int)

class PostResource(Resource):
    def get(self,post_id):#构造 /posts/1 GET 获取某条信息
        post_id =int(post_id)#终端发送过来的是json(str)格式的的请求url,post_id也是str
        abort_if_postnt_exist(post_id)
        result= Post.get(Post.id == post_id)
        title=result.title
        content=result.content
        return {"title":title,"content":content}

api.add_resource(PostResource,"/posts/<post_id>")#将Post类作为服务，并挂载到“/posts/<post_id>”,<xxx>代表参数id

if __name__=="__main__":
    app.run(debug=True)



