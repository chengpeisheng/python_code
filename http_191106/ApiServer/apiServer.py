#coding:utf-8
from flask import Flask,request,g
from flask_restful import reqparse,abort,Api,Resource

#引进model
from peewee import *
db=SqliteDatabase("posts.db")#创建一个数据库posts.db

class Post(Model):#创建一个Post表，这个表继承了Model类的所特性，
    title=CharField(unique=True)#创建一个char类型的title字段，并且是唯一的
    content=TextField()#创建一个text类型的content字段
    class Meta:#内嵌一个Meta类
        database=db

#创建一个app服务，并生成对应api接口框架
app = Flask(__name__)#定义一个app对象
api=Api(app)#给app生成对应的接口api

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

#引入数据库后改列表就不在使用
#定义一个列表
# POSTS=[
#     {},
#     {"title":"first post","content":"first post"},
#     {"title":"second post","content":"second post"},
#     {"title":"third post","content":"third  post"}
# ]

#对每个post_id进行判断是否异常,异常则退出，报错
def abort_if_postnt_exist(post_id):
    # try:
    #     POSTS[post_id]
    # except IndexError:
    #     abort(404,message="POSTS doesn~t exist")

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
        # post_id =int(post_id)#终端发送过来的是json(str)格式的的请求url,post_id也是str
        # abort_if_postnt_exist(post_id)
        # return POSTS[post_id]
        #把上面的表达方式修改成对数据库操作
        result= Post.get(Post.id == post_id)
        title=result.title
        content=result.content
        db.close()
        return {"title":title,"content":content}

    def delete(self,post_id):# 构造 /posts/1 DELETE 删除某条信息
        # post_id = int(post_id)  # 终端发送过来的是json(str)格式的的请求url,post_id也是str
        # abort_if_postnt_exist(post_id)
        # del POSTS[post_id]
        # return "delete successfully"
        # 把上面的表达方式修改成对数据库操作
        result=Post.get(Post.id==post_id).delete_instance()
        if result==1:
            return  "删除成功",201 #规定了201 、202 203状态码都是有成功提示语，唯独204即使给出提示语，也不打印
        else:
            return "删除失败",401

    def put(self,post_id):# 构造 /posts/1 PUT 修改某条信息
        # json_data=request.get_json(force=True)#
        # post_id=int(post_id)
        # abort_if_postnt_exist(post_id)
        # post = {"title": json_data["title"], "content": json_data["content"]}
        # POSTS[post_id] = post
        # return post
        # 把上面的表达方式修改成对数据库操作
        post_id = int(post_id)
        json_data=request.get_json(force=True)#
        Post.update(title=json_data["title"]).where(Post.id==post_id).execute()
        Post.update(content=json_data["content"]).where(Post.id == post_id).execute()
        return  201



class PostListResource(Resource):
    def get(self):#构造 /posts GET 获取所有信息
        # posts=[]
        # for post in POSTS:
        #     if post :
        #         new_post = {}
        #         new_post["url"]="/posts/"+str(POSTS.index(post))
        #         new_post["title"]=post["title"]
        #         posts.append(new_post)
        # return posts

        #把上面的语句修成对数据库的操作
        posts=[]
        results=Post.select()#取出所有表中数据
        for result in results:#循环赋值给变量post，并将变量post粘贴到数组posts中一起返回
            post={"title":result.title,"content":result.content}
            posts.append(post)
        return posts

    def post(self): # 构造 /posts POST  创建某条信息
        # json_data=request.get_json(force=True)#将发送的json数据转为dict
        # post_id=len(POSTS)
        # POSTS.append({"title":json_data["title"],"content":json_data["content"]})#将字典加入到列表中
        # return POSTS[post_id],201
        # 把上面的语句修成对数据库的操作
        json_data = request.get_json(force=True)  # 将发送的json数据转为dict
        try:
            Post.create(title=json_data["title"],content=json_data["content"])
            result=Post.get(Post.title==json_data["title"])
            return result.title,result.content,201
        except IntegrityError:
            return {"message":"title is already token"} , 401



api.add_resource(PostResource,"/posts/<post_id>")#将Post类作为服务，并挂载到“/posts/<post_id>”,<xxx>代表参数id
api.add_resource(PostListResource,"/posts")#将PostList类作为服务，并挂载到“/posts

if __name__=="__main__":
    app.run(debug=True)



