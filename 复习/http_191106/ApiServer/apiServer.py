#coding:utf-8
###########################################第一种方法：数据暂存列表中##################################################
# from flask import Flask
# from flask_restful import Api,Resource,abort,request
#
# POSTS = [
# 	{},
#     {'title': 'first post', 'content': 'first post'},
#     {'title': 'last post', 'content': 'last post'},
#     {'title': 'how to learn interface test', 'content': 'how to learn interface test'}
# ]
#
# #定义一个判断Post[post_id]是否在列表内
# def abort_if_postid_doesnot_exit(post_id):
#     post_id=int(post_id)
#     try:
#         POSTS[post_id]
#     except IndexError:
#         abort(401,message="post_id超出范围！")
#
# app=Flask(__name__)#定义一个Flask框架，
# api=Api(app)#定义个Api框架
#
# #构造资源Post,一个资源就是一个class
# class Post(Resource):
#     def get(self,post_id):#定义一个get方法，/posts/1
#         abort_if_postid_doesnot_exit(post_id)#判断是否超出范围
#         post_id=int(post_id)#确保输入的post_id是int
#         return POSTS[post_id]
#
#     def put(self,post_id):#定义一个put方法，/posts/1
#         abort_if_postid_doesnot_exit(post_id)#判断是否超出范围
#         post_id = int(post_id)#确保输入的post_id是int
#         json_data=request.get_json()#捕获发送的数据，把dict数据以json格式显示
#         post={"title":json_data["title"],"content":json_data["content"]}
#         POSTS[post_id]=post
#         return POSTS[post_id]
#
#     def delete(self,post_id):#定义一个delete方法，/posts/1
#         abort_if_postid_doesnot_exit(post_id)
#         post_id = int(post_id)  # 确保输入的post_id是int
#         del POSTS[post_id]
#         return  "delete success!"
#
# #构造资源PostList,一个资源就是一个class
# class PostList(Resource):
#     def get(self):#定义一个get方法，/posts
#         posts=[]
#         for post in POSTS:
#             if post :
#                 new_post = {}
#                 new_post["url"]="/posts/"+str(POSTS.index(post))
#                 new_post["title"]=post["title"]
#                 posts.append(new_post)
#         return posts
#
#     def post(self):
#         post_id = len(POSTS)
#         json_data=request.get_json(force=True)#获取发送的body.将dict数据已json格式显示
#         post={"title":json_data["title"],"content":json_data["content"]}
#         POSTS.append(post)
#         return POSTS[post_id]
#
#
# #将资源挂载到api，并规定访问路由
# api.add_resource(Post,"/posts/<post_id>")
# api.add_resource(PostList,"/posts")
# if __name__=="__main__":
#     app.run(debug=True)


#######################################第二种方法：数据通过peewee存入Sqlite3中#########################################
#coding:utf-8
from flask import Flask,g
from flask_restful import Api,Resource,abort,request

app=Flask(__name__)#定义一个Flask框架，
api=Api(app)#定义个Api框架

#引入model
from peewee import *
db=SqliteDatabase("post.db")#如果是第一次，运行则是创建数据库，否则是指定要连接的数据库

class Post(Model):#创建Post表，并规定字段类型
    title=CharField(unique=True)
    content=TextField()
    class Meta():
        database=db

@app.before_request
def berore_request():
    g.db=db
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

#定义一个判断是否在数据库内
def abort_if_postid_doesnot_exit(post_id):
    post_id=int(post_id)
    try:
        Post.get(Post.id==post_id)
    except Post.DoesNotExist:
        abort(401,message="post_id超出范围！")

#构造资源PostResource,一个资源就是一个class
class PostResource(Resource):
    def get(self,post_id):#定义一个get方法，/posts/1
        abort_if_postid_doesnot_exit(post_id)#判断是否超出范围
        post_id=int(post_id)#确保输入的post_id是int
        data=Post.get(Post.id==post_id)
        response={"title":data.title,"content":data.content,"url":"http://127.0.0.1:5000/posts/"+str(data.id)}
        return response

    def put(self,post_id):#定义一个put方法，/posts/1
        abort_if_postid_doesnot_exit(post_id)#判断是否超出范围
        post_id = int(post_id)#确保输入的post_id是int
        json_data=request.get_json()#捕获发送的json数据，把json数据转化为dict格式显示
        Post.update(title=json_data["title"]).where(Post.id==post_id).execute()#修改title
        Post.update(content=json_data["content"]).where(Post.id == post_id).execute()#修改content
        data=Post.get(Post.id==post_id)
        response={"title":data.title,"content":data.content,"uri":"http://127.0.0.1:5000/posts/"+str(data.id)}
        return response

    def delete(self,post_id):#定义一个delete方法，/posts/1
        abort_if_postid_doesnot_exit(post_id)
        post_id = int(post_id)  # 确保输入的post_id是int
        Post.get(Post.id==post_id).delete_instance()#删除实例
        return  "delete success!"

#构造资源PostList,一个资源就是一个class
class PostList(Resource):
    def get(self):#定义一个get方法，/posts
        list=[]
        data=Post.select()
        for d in data:#把数据库的数据取出来，重新组成列表返回
            list.append({"title":d.title,"content":d.content,"uri":"http://127.0.0.1:5000/posts/"+str(d.id)})
        return list

    def post(self):
        json_data = request.get_json(force=True)  # 获取发送的body.将dict数据已json格式显示
        try:
            Post.create(title=json_data["title"], content=json_data["content"])#判断title是否重复，重复报错
        except IntegrityError:
            return "title不能重复，请重新填写！"
        post_id=Post.get(Post.title==json_data["title"]).id
        uri="http://127.0.0.1:5000/posts/"+str(post_id)
        return {"uri":uri,"status":"success"}


#将资源挂载到api，并规定访问路由
api.add_resource(PostResource,"/posts/<post_id>")
api.add_resource(PostList,"/posts")
if __name__=="__main__":
    app.run(debug=True)
