# -*- coding:UTF-8 -*-
#coding:UTF-8
#############################################python程序练习题集(A-1)

#1.
#方法一：lam函数法
# a=1
# b=2
# c=3
# d=4
# func=lambda a,b,c,d:a+b-c*d
# print(func(a,b,c,d))

#普通函数定义法
# def func(a,b,c,d):
#     return a+b-c*d
# a=1
# b=2
# c=3
# d=4
# e=func(a,b,c,d)
# print(e)

#2.
#方法一：普通函数法
# def area(a,b):
#     return a*b
# def perimeter(a,b):
#     return 2*(a+b)
# a=10
# b=10
# s=area(a,b)
# l=perimeter(a,b)
# print(s,l)

#lambda函数法
# area=lambda a,b:a*b
# perimeter=lambda a,b:2*(a+b)
# print(area,perimeter)#打印函数的地址
# a=10
# b=10
# s=area(a,b)
# l=perimeter(a,b)
# print(s,l)


#3.
#py2的9/2=4，py3的时候9/2=4.5
#py2的写法
# a=9
# b=2
# c=float(a)/float(b)
# print(c)

#py3的写法
# a=9
# b=2
# c=a/b
# print(c)


#4.
#方法一:while循环法
# n=0
# s=1
# while n<4:
#     s=s*7
#     n+=1
# print(s)

#方法二:for循环法
# s=1
# for i in range(1,5):
#     s=s*7
# print(s)
#方法三：函数法pow()
# x=7
# y=4
# z=pow(x,y)
# print(z,d)


#5.
# n=0
# while n<10:
#     C=float(input("请输入摄氏温度="))#输入的温度，input()函数输入的是str类型，必须int()转换后才可以进行运算
#     print(C)
#     translation=lambda x:float(5)/float(9)*(x-32)#用lambda函数定义一个无名的临时函数，并将这个临时函数赋给变量translation，
#     print("现在的华氏温度=",translation(C))#translation变量名字就和临时函数绑定了，调用改临时函数
#     print(type(C))
#     print("############")



#6.
# n=0
# while n<1:
#     original_price=float(input("请输入原始价格="))#输入价格，并float化
#     if original_price<50:
#         print("最终价格=",original_price)
#     elif original_price>=50 and original_price<=100:
#         print("最终价格=",0.9*original_price)
#     else:
#         print("最终价格=",0.8*original_price)

#7.
# n=0
# while n<1:
#     number=int(input("请输入一个数字："))
#     if number%3==0 and number%5==0:
#         print("你输入的数可以同时被3和5整除！")
#     else:
#         print("你输入的数不可以同时被3和5整除！")


#8.
# s=0
# i=1
# for i in range(1,101):
#     s=s+i
# print(s)

#9.
# a=int(input("please input first number a:"))
# b=int(input("please input second number b:"))
# c=a
# a=b
# b=c
# print("a=",a,"b=",b)

#10.
# a=int(input("please input first number :"))
# b=int(input("please input second number :"))
# c=int(input("please input third number :"))
# max_number=max(a,b,c)
# print(max_number)



#11.
# n=0
# def leapYear(year):
#     if year%4==0 and year%100!=0:
#         print("this is a LeapYear!",year)
#     elif year%400==0:
#         print("this is a LeapYear!",year)
#     else:
#         print("this is not a Year!")
# while n<1:
#     year=int(input("please input a LeapYear="))
#     leapYear(year)


#12.
# times=10
# list10=[]
# name=[]
# sex=[]
# age=[]
# num=0
# for i in range(times):
#     n=input("please input name: ")#py3中raw_input和input 2个函数，只保留了input函数，返回值全按str类型
#     name.append(n)
#     s=input("please input sex: ")#py3中raw_input和input 2个函数，只保留了input函数，返回值全按str类型
#     sex.append(s)
#     a=input("please input age: ")#py3中raw_input和input 2个函数，只保留了input函数，返回值全按str类型
#     age.append(a)
#
#
#     if sex[i]=='girl'and int(age[i])>=10 and int(age[i])<=12:
#         print("yes,welcome to join us!")
#         num+=1
#     list10.append(name[i]+","+sex[i]+","+age[i])
# print(list10)
# print(num)


#13.
# a=[]
# for i in range(127):
#     a.append(chr(i+1))
# print(a)
#ord()函数是用来返回字符的ASCII码的顺序，chr()函数是用来返回ASCII码对于的字符


#14.
# num=3
# s=float(input("请输入消费总额："))
# total=s*1.15
# per=total/3
# print(per)

#15.
#太无聊，这题，不做了

#16.
# while 1<2:
#     import  random
#     first=int(input("please input first number="))
#     second=random.randint(1,5)
#     print(second)
#     if first>second:
#         print("bigger")
#     elif first<second:
#         print("lower")
#     else:
#         print("equal")

#17.
#略


#18.
# import random
# li1=[]
# li2=[]
# for i in range(10):
#     li1.append(random.randint(1,10))
# print(li1)
# for i in range(len(li1)):
#     li2.append(li1[len(li1)-1-i])
# print(li2)

#19.
#略

#20.
#略

#21.
#略

#22.
# def factorial(n):
#     s = 1
#     for i in range(1,n+1):
#         s=s*i
#     print(s)
#
# factorial(0)


#23.
# def judeg(x):
#     g=x%10
#     if g>=1 and g<=5:
#         print(x)
#
# for i in range(10,50+1):
#     n=judeg(i)
#


#24.
#同13题

#25.
#略

#26.
#略

#27.
#略

#28.
# import random
#
# def createNum(n):#创建3个[10,1000]的随机数，并将随机数append到li尾部，打印最后的li
#     # global li#定义li为全局变量，并能在函数内修改值，
#     for i in range(n):
#         a=random.randint(10,1000)
#         li.append(a)
#     print(li)
#
# def compare(list):#
#     topone=max(list)
#     print(topone)
#
# li=[]
# createNum(3)
# print(li)#打印li看在函数内是否被修改
# compare(li)

#29.
# import  random
#
# def gcd(a,b):
#     min = compare(a, b)
#     li = []
#     for i in range(1, min + 1):  # 从1到min，挨个作为a,b的除数，找到能被整除的数，
#         # 然后追加到列表里，然后找到列表中最大的数
#         if a % i == 0 and b % i == 0:
#             print("公约数=", i)
#             li.append(i)
#
#     maxone=max(li)
#     print("max=",maxone)
#
# def compare(a, b):  # 找出最小的数，以最小的数为标尺，从1开始一个个推算，
#     # 算到最后一个既可以被最大数整除，又可以被最小数整除，就找到最大公约数了
#     if a > b:
#         return b
#     else:
#         return a
#
# a = random.randint(10, 100)
# print("a=", a)
# b = random.randint(10, 100)
# print("b=", b)
# gcd(a,b)

#求最小公倍数
# import random
#
# def compare(a, b):  # 找出最大的数，以最大的数为标尺，从大开始一个个推算，
#     # 算到第一个既是a的倍数，又是b的倍数，就找到最小公倍数
#     if a > b:
#         return a
#     else:
#         return b
#
# def lcm(a,b):
#     max=compare(a,b)
#     n=0
#     i=1
#     while n<1:
#         if i*max%a==0 and i*max%b==0:
#             min=i*max
#             # n+=1
#             break
#         else:
#             i+=1
#     print("找到最小公倍数=",min)
#
# a = random.randint(10, 20)
# print("a=", a)
# b = random.randint(10, 20)
# print("b=", b)
# lcm(a,b)



#######从0到99中查找输入的值
# x=int(input("请输入X:"))
# y=0
# for y in range(0,100):
#     if x==y:
#         print("找到数字：",x)
#         break
#     else:
#
#         print("没找到")




#######continue练习
# x=0
# for i in [1,2,3,4,5]:
#     if x==i:#相等则不进行任何操作，执行下一条循环，不等则x累加
#         continue
#     else:
#         x+=i
# print(x)


#reduce()累加[1,2,3,4,5,6,7,8,9]
# def add(x,y):
#     return x*y
# sum1=reduce(add,[1,2,3,4,5,6],7)
# print(sum1)
# print("############")
# sum1=1
# for i in range(1,8):
#     sum1=sum1*i
# print(sum1)






























