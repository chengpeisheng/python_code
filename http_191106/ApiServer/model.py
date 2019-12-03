from peewee import *
db=SqliteDatabase("posts.db")#创建一个数据库posts.db

class Post(Model):#创建一个Post表，这个表继承了Model类的所特性，
    title=CharField(unique=True)#创建一个char类型的title字段，并且是唯一的
    content=TextField()#创建一个text类型的content字段
    class Meta:#内嵌一个Meta类
        database=db

db=SqliteDatabase("movies.db")#创建一个数据库posts.db
class Movies(Model):#创建一个Post表，这个表继承了Model类的所特性，
    name=CharField(unique=True)#创建一个char类型的title字段，并且是唯一的
    type=TextField()#创建一个text类型的content字段
    class Meta:#内嵌一个Meta类
        database=db

"""
创建一个数据库模型，定义好
数据库：students.db
Marks：表
字段：name、identification_number、score
"""
db=SqliteDatabase("students.db")#加载Model.py文件后就会产生一个students.db文件
class Marks(Model):#定义表Marks 相关字段，表继承Model属性，
    name=CharField()
    identification_number=TextField(unique=True)
    score=CharField()
    class Meta():
        database=db