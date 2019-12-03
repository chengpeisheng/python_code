from peewee import *#peewee 支持Sqlite、MySQL、postgresql、
db=SqliteDatabase("post.db")#定义一个数据库post，当使用db.connect()就会产生post.db数据库

class Post(Model):#给数据库定义一个Post表
    title=CharField(unique=True)
    content=TextField()

    class Meta:#将数据存入数据库
        database=db