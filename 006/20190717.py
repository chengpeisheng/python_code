# -*- coding:UTF-8 -*-
#coding:UTF-8
# 当使用python2进行编程时，并且有非英文的字符插入进去，必须使用UTF-8消除编译错误

##############################################while语句练习########################## #
#
# num=2
# while num<=101:
#     print (num)
#     num=num+1
# else:
#     print(num)



# num=1
# while num<=100:
#     if (num%2==1) :
#         print (num)
#     num=num+1

# num=1
# while num<=100:
#     if num%3==0:
#         print (num)
#     num=num+1

# import math
# a=1
# s=0
# while a<=9:
#     s=s+math.pow(a,2)
#     a=a+1
# print (int(s))
import math
# a=4
# s=math.factorial(a)
# print(s)

#import math
#
# i=100
# while i<=999:
#     b = int(i / 100)
#     s = int((i - b * 100) / 10)
#     g = int(i - b * 100 - s * 10)
#     if i==b**3+s**3+g**3:
#         print (i,b,s,g)
#     i=i+1


##############################################字符串练习##########################
#打印字符a、p、k的位置#
# s="235apk"
# num=0
# print("the length fo s is ",len(s))
#
# while num<len(s) :
#     if "a" == s[num] or "p" == s[num] or"k" == s[num]:
#         print(num+1,s[num])
#     num=num+1
# else:
#     print("end")
#


######################遍历打印字符s,并统计字符串的中字母a出现的次数和位置################
# s='23asdf45asga5apk'
# print("字符串s长度为：",len(s))
# num=0
# num1=0
# while num <len(s):
#     if 'a'==s[num]:
#         print("a的位置为：",num+1)
#         num1=num1+1
#     num=num+1
#
# else:
#     print("end")
#     print('a一共出现：',num1,'次')

#########################################打印you000-you100############################
# s1='you'
# s2="00"
# s3="0"
# num=0
#
# while num<100:
#     if num<10:
#         print(s1+s2+str(num))
#     elif num<100:
#         print(s1 + s3 + str(num))
#     num=num+1
# else:
#     print(s1 + "100")



################用random.randint随机产生一个6位数，①判断此数里是否含有4和7及出#########
################现的位置②在没有4和7的情况下，有没有6和8
#
# import random
# num4=0#统计4出现的次数
# num7=0#统计7出现的次数
# num47=0#统计4 、7出现的次数
# num0=0#统计循环次数
# num=0#保存随机数
# while num0<100:#统计循环次数
#     num= random.randint(10, 50)  # 随机数[100000,999999]
#     if '4'in str(num) and '7'in str(num):
#         print("有4和7在里面：",num)
#         num47=num47+1#统计4 7 同时出现的次数
#     elif '7'in str(num):
#         print("有7在里面：",num)
#         num7 = num7 + 1
#     elif '4'in str(num):
#         print("有4在里面：",num)
#         num4 = num4 + 1
#     num0=num0+1
# print('#######################')
# print("仅出现4的次数：",num4)
# print("仅出现7的次数：",num7)
# print("同时出现4、7的次数：",num47)



#########################int---str、int---chr之间的转化#########################

#chr ---ord   、int---str
#chr(97)="a"  ord("a")=97
#int("97")=97  str(97)="97"
# print(chr(97))
# print(type(chr(97)))
#
# print(ord("a"))
# print(type(ord("a")))
#
# print(int("97"))
# print(type(int("97")))
#
# print(str(97))
# print(type(str(97)))
#












#####################构造字符串“a01b02c03........y25z26”#####################
#int(字符串)    把字符串转化为整型
# chr(ascii)    把ascii转化为字符
# ord(字符)     把字符转化为ascii

# print(int("01"))
# print(chr(97))
# print(ord('a'))
#
# s1="a"#字符a的ascii值为97
# s2="01"#字符01的ascii值为97
# print(ord(s1))
# print(int(s2))
# a b c d   97 98 99
#
# a=97
# b=1
# num1=1
# string=""
#
# while num1<=26 :
#     if num1<=9:
#         string=string+chr(a)+"0"+str(b)
#     else:
#         string=string+chr(a)+str(b)
#     num1=num1+1
#     a = a + 1
#     b = b + 1
# print(string)







######################  利用chr（ASCII转字符），和ord(字符转ASCII)，
####################### int（字符串转整形）实现翻译“#98#102#132#12#66#90#22#”

# string1="#98#102#132#12#66#90#22#"
# num1=0
# num2=0
# string2=""
# while   num1<len(string1):
#     if  string1[num1]=="#":
#
#         string2=string2+string1[num1]
#         num1 = num1 + 1
#     else:
#         string2=string2+chr(int(string1[num1]))
#         num1 = num1 + 1

#
# print(string2)




#####################将”hello world”翻译成对于的ASCII值
# string1="hello world"
# string2=""
# num2=0
# while   num2<len(string1):
#     #print(string1[num2],ord(string1[num2]))
#     string2=string2+str(ord(string1[num2]))+"#"
#     num2=num2+1
# print(string2)



# ？？？？？？？？？？？？翻译这个语句104#101#108#108#111#32#119#111#114#108#100#

# def multiply(a, b):
#     a=input("请输入a:")
#     b=input("请输入b:")
#     c=int(a)*int(b)
#     print("a和b的乘积是：",c)




###############################判断s字符串在m字符串中是否存在，存在的数量，和存在的位置##########################
# m="cpcpcpcpcpcpc"
# #  01234
# s="cpc"
# x=0
# w=0
# if s in m :
#     while x < len(m) - len(s) + 1:
#         y = 0
#         z = 0
#         while y < len(s):
#             if s[y] == m[x + y]:
#                 z += 1
#                 if z == len(s):
#                     w+=1
#                     print(x, s)
#             y += 1
#         x += 1
#     print("s在m中的数量为",w)
# else:
#     print("s not in m")







#####切片方法的使用：判断子串是否存在主串中,并打印出现的数量和位置##########################
#string slice
# m="cpc1pcpcpcpcpc"
# # #  01234
# s="cpc1"
# x=0
# if s in m:
#     while x<len(m)-len(s)+1:
#         if m[x:x+len(s)]==s[:len(s)]:
#             print(x,s)
#         x+=1
#
# else:
#     print("s not in m")
# # print(s[:len(s)])


####字符串的切片：sub1=”hello the cool world”,sub2=”welcome to ”,
# 请将2个字符进行操作，得到sub4=”welcome to the cool world ”.
# 提示：2种方法，分别利用while循环和切片知识
#方法一：索引方法进行字符串截取和合并
# sub1="hello the cool world"
# sub2="welcome to"
# sub3="the cool world"
# sub4=""
# x=0
# while x<len(sub1)-len(sub3)+1:
#     y=0
#     z=0
#     while y<len(sub3):
#         if sub1[x+y]==sub3[y]:
#             z+=1
#             if z==len(sub3):
#                 print("find the sub3",x)
#                 w=0
#                 while w<len(sub3):
#                     sub4=sub4+sub1[x+w]
#                     w+=1
#         y += 1
#     x+=1
# sub4=sub2+" "+sub4
# print(sub4)

# #方法二：切片方法进行字符串截取和合并
# sub1="hello the cool world"
# sub2="welcome to"
# sub3="the cool world"
#
#
# sub4=""
# x=0
# while x<len(sub1)-len(sub3)+1:
#     y=0
#     z = 0
#     while y<len(sub3):
#         if sub1[x+y]==sub3[y]:
#             z+=1
#             if z==len(sub3):
#                 print("find the sub3",x)
#                 sub4=sub4+sub2+" "+sub1[x:x+len(sub3)]+" "
#         y+=1
#
#     x+=1
#
# print(len(sub4),sub4)



######################①将语句sub1=" you cps love "中的空格删除，并将得到的语句中完整的单词逐个输出来
# sub1=" y  o u c  ps   l o v e "
# sub2=""
# i=0
# n=0
# while i<len(sub1) :
#     if sub1[i]!=" ":
#         sub2=sub2+sub1[i]
#     else:
#         print("空格")
#         n+=1
#
#     i+=1
# print("空格个数=",n,"删除空格后的字符串为：",sub2)





#####################将语句sub1=" you cps love "中的空格用字符@替代空格，将sub1输出
# sub1=" you cps love "
# i=0
# sub2=""
# while i<len(sub1):
#     if sub1[i]!=" ":
#         sub2+=sub1[i]
#     else:
#         sub2=sub2+"@"
#     i+=1
# print("最终结果为：",sub2)






##################################利用字符串的切片寻找子串在字符串的位置
#####sub1="youme",sub2="me",找出字符串sub2在sub1的位置
# sub1="youme"
# sub2="me"
# i=0
#
# if sub2 in sub1:
#     print("sub2 in sub1")
#     while i<len(sub1)-len(sub2)+1:
#         j=0
#         n=0
#         while j<len(sub2):
#             if sub1[i+j]==sub2[j]:
#                 n+=1
#                 if n==len(sub2):
#                     print("sub2 在sub1的位置为：",i)
#             else:
#                 break
#             j+=1
#         i+=1
# else:
#     print("sub2 not in sub1")






####################删除母串中指定的子串###################################
#sub1="youme56@shime"   sub2="me"  删除sub1中sub2,并输出sub1,首先判断sub2在sub1的个数，
#多次删除里面的sub2,出现一次做一次遍历
######################################################################
# sub1="youme56@shime"
# sub2="me"
# sub3=""
# i=0
#
# if sub2 in sub1:
#     print("sub2 in sub1")
#     print("sub2的数量为：",sub1.count(sub2))
#     while i<len(sub1)-len(sub2)+1:
#         j=0
#         n=0
#         while j<len(sub2):
#             if sub1[i+j]==sub2[j]:
#                 n+=1
#                 if n==len(sub2):
#                     print("sub2在sub1的位置是：",i)
#                     sub3=sub1[:i]+sub1[i+len(sub2):]
#                     print(sub3)
#                     k=0
#                     sub4=""
#                     while k<len(sub3)-len(sub2)+1:
#                         p=0
#                         q=0
#                         while p<len(sub2):
#                             if sub3[k+p]==sub2[p]:
#                                 q+=1
#                                 if q==len(sub2):
#                                     print("sub2在sub1的位置是：",k)
#                                     sub4=sub3[:k]+sub3[k+len(sub2):]
#                                     print(sub4)
#                             p+=1
#                         k+=1
#             else:
#                 break
#             j+=1
#         i+=1
#
# else:
#     print("sub2 not in sub1")


##############isspeace函数的使用
#
#
#
#


# sub1="  2  "
# if sub1.isspace()==True:
#     print (1)
# else:
#     print(0)




##############find.rfind、count函数的使用
#s.find(sub[,start[,end]])在字符串s中找到sub字符串，并打印最小的索引，可以指定start、end
#s.rfind(sub[,start[,end]])在字符串s中找到sub字符串，并打印最大的索引，可以指定start、end
# #当没找到sub就返回-1
# sub1="you me meyou hi,"
# sub2="me"
# if sub1.count(sub2)>0:
#     i=sub1.find(sub2)
#     j=sub1.rfind(sub2,5)
#     print(sub1.count(sub2),i,j)

##############replace函数的使用
#str.replace(old,new[,count=-1]),将字符串str中old替换成new,count默认-1，替换全部，若指定数字，代表替换个数
# self="aabbcaacddaa"
# old="aa"
# new="##"
# print(self.replace(old,new))
# help()



##########################strip函数的使用
#str.strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#str.strip = strip(self, chars=None, /)
#Return a copy of the string with leading and trailing whitespace remove.If
#chars is given and not None, remove,characters in chars instead.
# old="qw000#00003210Runoob01230000000wq"
# new=old.strip("qw")
# print(new)








###############创建列表list=[“apple”,”banana”,”grape”,”orange”],
# 在列表末尾添加元素”watermelon”；在列表 第一个元素中添加一个元素”grapefruit”;
# 在列表中移除grape;从列表中移除”a”；使用pop打印从列表中探出的元素

# list=["apple","banana","grape","orange"]
# print(list)
# list.append("watermelon")
# print(list)
# list.insert(1,"grapefruit")
# list.insert(0,"grapefruit")
# print(list)
# #list.remove("grape")
# list.remove("grapefruit")
# #list.remove("a")
# print(list)





################################################################################
#创建list=["apple","banana","grape","orange"],输出list[-2];输出list[1:3];输出list[-3:-1]
# 遍历打印列表list=[["apple","banana"],["grape","orange"],["watermelon"],["grapefruit"]]
#list=['apple',"banana","grape","orange"]
# list=[["apple","banana"],["grape","orange"],["watermelon"],["grapefruit"]]
# print(list)
# print(len(list))
# print(list[-2])
# print(list[2])
# print(list[1:3])
# print(list[-3:-1])
#
# for i in range(len(list)) :
#     for j in range(len(list[i])):
#         print(list[i][j])






################################################列表的连接#########################################################
# list1=["apple","banana"]
# list2=["grape","orange"]
# list1.extend(list2)
# print(list1)
# list3=["apple1","banana1"]
# list4=["grape1","orange1"]
# list3=list3+list4
# print(list3)
# list5=["apple2","banana2"]
# list6=["grape2","orange2"]
# list5+=list6
# print(list5)



###########################################排序######################
#[110,215,175,319,21,6]找出列表中最大的数max1和第二大的数max2
#[110,215,175,319,21,6]找出列表中最小的数min1和第二小的数min2
# li1=[110,215,175,319,921,6]
# li2=["a","g","b","c"]
# li1.sort()
# li2.sort()
# print(li1)
# print("max1=",li1[len(li1)-1])
# print("max2=",li1[len(li1)-2])
# print(max(li1))
# print(max(li2))
#
# li1.reverse()
# li2.reverse()
# print(li1)
# print("min1=",li1[len(li1)-1])
# print("min2=",li1[len(li1)-2])



###################Li1=[1,2,3,4,5,6,7,8,9,10],li2=[1,2,3,4,5,6,7,8,9,10,11],
# 用range函数产生这2个列表，并将2个列表的每个数据相加后输出
# li1=[]
# for i in range(1,11):
#     li1.append(i)
# print(li1)
# li2=[]
# for j in range(1,12):
#     li2.append(j)
# print(li2)
# ###方法一
# k=0
# while k<10:
#     li2[k]=li1[k]+li2[k]
#     k+=1
# print(li2)
#方法二
# for k in range(0,10):
#     li2[k]=li1[k]+li2[k]
# print(li2)
#方法三，此处错误是：li3是空列表，print(len(li3))长度只有0,所以li3[k]每次赋值都会产生索引超出range
#li3=[]#IndexError: list assignment index out of range
# print(len(li3))
# for k in range(0,10):
#     li3[k]=li1[k]+li2[k]
# print(li3)




#############列表li=[1,[2,[3,[4,5,6],7],8,],9,10,11,12],中每个数字打印出来
# li=[1,[2,[3,[4,5,6],7],8,],9,10,11,12]
# # if type(li)==list:
# #     print("ok")
# print("len(li)=",len(li))
# for i in range(len(li)):#遍历第一层层列表
#     # print("li[i]=",li[i])
#     if type(li[i])==list:#判断第二层是否是列表
#         for j in range(len(li[i])):#遍历第二层列表，并打印
#             if type(li[i][j])==list:  # 判断第三层是否是列表
#                 for k in range(len(li[i][j])):  # 遍历第三层列表，并打印
#                     if type(li[i][j][k]) == list:  # 判断第三层是否是列表
#                         for m in range(len(li[i][j])):  # 遍历第三层列表，并打印
#                             print(li[i][j][k][m])
#                     else:
#                         print(li[i][j][k])
#             else:
#                 print(li[i][j])
#     else:
#         print(li[i])



###########元组 列表 字符串的访问和赋值，他们之间的区别
#             访问        赋值
#元组         tuple[2]    元组是常量不可以赋值
#列表         li[2]      append/extend
#字符串       str[4]     字符串是常量不可以赋值的
#
# li=[1,2]
# li.append(3)
# li.extend(li)
# print(li)
# print(li[0])#列表可以索引访问
#
#
# str="01234"
# print(str[4])
# # str[0]='@'#字符串是常量，不可以赋值的
# print(str)
#
# tuple=(12,"ad","asd")
# print(tuple[2])
# #tuple[2]="23"#元组是常量不可以赋值
# print(tuple[2])








##########################str=”hello jeapedu com www”,将字符串str中字符逐个切割出来，并以列表的形式展示
# li=[]#建立空列表
# str="hello jeapedu com www"
# print(len(str))
# for i in range(len(str)):
#     #li.append(str[i])#将字符串的每个字符添加到列表中
#     li.extend(str[i])#将字符串的每个字符追加到列表中
# print(li)
#
#






# li1=range(1,10)#python 2编译环境时，range函数产生了一个新的列表；python 3编译环境时，range函数并未产生列表，仍是range(1, 10)
# li2=list(li1)
# print(li2)





#########str="hello world ,welcome to you !",tuple=(123,"asd","你好",有)
# str="hello world ,welcome to you !"
# tuple1=(123,"asd","你好",2.36)
# li=[123,"asd","你好",2.36]
# li1=list(str)#字符串--->列表
# print(li1)
# li2=list(tuple1)#元组--->列表
# print(li2)

# li=[123,"asd","你好",2.36]
# str1=str(li)
# for i in range(len(str1)):
#     print(str1[i])





#######S=”hello::jeapedu::com::www”,将字符串中sub=’::’删除掉，
# 并将字符串s和sub之间的字符逐一展示出来li=[‘hello’,’jeapedu’,’com’,’www’,’www’]
# S="hello::jeapedu::com::www"
# str1=S.split("::")#以"::"作为分割符切割，并将结果以列表的形式展示
# print(str1)




#############################################################################################################
# S=”hello jeapedu com www ”,将字符串s中字符逐个切割出来，并以列表的形式展示；
# 将字符串中s里面的单词完整切割出来并以列表展示li=[‘hello’,’jeapedu’,’com’,’www’];
# 以‘e’为分割点，将字符串s分割成三段，并以列表形式展示li=[‘h’,’llo j’,’ap’,’du com www’]
#
# S="hello  jeapedu comwww "
# li=list(S)#list函数可以将字符串转化为单个字符的列表
# print(li)
# li1=S.split("")
#
# print(li1)




######################统计字符串中某个字符出现的次数，并构造成函数
# def countSub(s,sub):
#     i=0
#     n=0
#     while i < len(s):
#         if s[i]==sub:
#             n+=1
#         i+=1
#     print(n)
#
# s1="553535@2@@@wer"
# sub1="@"
# countSub(s1,sub1)

######################统计字符串中子串出现的次数，并构造成函数
#方法一:逐一字符进行比较
# def countSub(s,sub):
#     count=0#代表子串出现次数
#     i=0#代表比较次数
#     while i<len(s)-len(sub):
#         j=0#代表子串比较次数
#         n=0
#         while j<len(sub):
#             if s[i+j]==sub[j]:
#                 n+=1
#                 if n==len(sub):
#                     print("find sub in :",i)
#                     count+=1
#             j+=1
#         i+=1
#
# s1="@@#"*3
# sub1="@@"
# print(s1)
# countSub(s1,sub1)

#方法二：切片和子串进行比较
# def countSub(s,sub):
#     i=0
#     count=0
#     while i<len(s)-len(sub):
#         if s[i:i+len(sub)]==sub:
#             count+=1
#         i+=1
#     print(count)
#
# s1="@@#"*5
# sub1="@@"
# print(s1)
# countSub(s1,sub1)
#
#





########################统计字符串中单个字符或者子字符串出现的次数，并构造成函数
# def countChar(s,sub):
#     i=0
#     n=0
#     while i < len(s):
#         if s[i]==sub:
#             n+=1
#         i+=1
#     print("子串出现次数：",n)
#
# def countString(s,sub):
#     count=0#代表子串出现次数
#     i=0#代表比较次数
#     while i<len(s)-len(sub):
#         j=0#代表子串比较次数
#         n=0
#         while j<len(sub):
#             if s[i+j]==sub[j]:
#                 n+=1
#                 if n==len(sub):
#                     print("find sub in :",i)
#                     count+=1
#             j+=1
#         i+=1
#     print("子串出现次数：",count)
#
# s1="@@#"*3
# sub1="@@"
# print(s1)
# print(sub1)
# if len(sub1)==1:
#     countChar(s1,sub1)
# else:
#     countString(s1,sub1)






#####################findListMax函数，查找列表中最大的数值，和第二大的数值，
#方法一
# def findMaxList(list):
#
#     list1=list
#     list1.sort(reverse=True)#按照大小顺序分类排序
#     #list1.reverse()#list.reverse()函数用来逆序排列列表
#     print("降序排列后的list:",list1)
#     print("最大元素为：",list1[0])
#     print("第二大元素为：",list1[1])
#
# li=[45,12,589,54,54,12,100]
# findMaxList(li)




#方法二,将列表内的每个元素和maxNum比较，如果大于maxNum就赋值给他，遍历后就是最大的元素
# def findMaxList(list):
#     li=list
#     maxNum1=li[0]
#     maxNum2= li[0]
#     for i in li:
#         if i>maxNum1:
#             maxNum1=i
#         elif i>maxNum2:
#             maxNum2=i
#     print(maxNum1,maxNum2)
# li=[45,12,100,54,54,12,100]
# findMaxList(li)




###################################删除li1中10#####################################
#方法一：一次删除所有10，循环多次，利用切片，删除一个后里面i=i-1防止漏比较
# li1=[10,45,12,10,10,45,10,10,10,2]#li1为全局变量，函数体内要修改全局变量，必须使用global
# def delALL(value):
#     i=0
#     global li1
#     #如果有这句，li1这个全局变量可以在函数体内被访问且修改，如果没有这句，Li1只能被访问，不能被修改，
#     # 全局参数不可以在函数内部被修改，只能被访问；除非global这个全局参数
#     while i<len(li1):
#         if li1[i]==value:
#             li1=li1[:i]+li1[i+1:]#删除10出现的位置，列表长度减少1个，此时如果i不减1,就会导致漏下一个没比较
#             print(li1)
#             i-=1
#            #
#         i+=1
# delALL(10)





###################################删除li1中10#####################################
# help(list.remove)
#  L.remove(value) -- remove first occurrence of value.
#  Raises ValueError if the value is not present.
# li1=[10,45,12,10,45,10]
# num=li1.count(10)
# print num
# def delAll(value,key):
#     for i in range(key):
#         li1.remove(value)#每次删除列表中第一个value
# delAll(10,num)
# print li1
#





# li1=[10,45,12,10,45,10]#li1为全局变量，函数体内要修改全局变量，必须使用global
# def delOne(value):
#     i=0
#     global li1#如果有这句，li1这个全局变量可以在函数体内被访问且修改，如果没有这句，Li1只能被访问，不能被修改，
#     # 全局参数不可以在函数内部被修改，只能被访问；除非global这个全局参数
#     while i<len(li1):
#         if li1[i]==value:
#             print li1
#             li1=li1[:i]+li1[i+1:]
#             print li1
#             print("#################")
#         i+=1
#


###############################n^2幂,n=9,列表[1,4,9,...81]，不用pow函数。
# def createList(long):#创建一个[1,2,3....9]的列表
#     global li
#     li=[]
#     for i in range(1,long+1):
#         li.append(i)
#     print(li)
#     return li
#
# createList(9)#创建一个[1,2,3....9]的列表
# for i in range(9):
#     li[i]=li[i]*li[i]#计算
# print(li)







#################################li1=[1,2,3,4],li2=[2,3,4,5]求2个列表的积li3
#方法一：
# li1=[]
# li2=[]
# li3=[]
# for i in range(1,5):
#     li1.append(i)
#     li2.append(i+1)
#     z=li1[i-1]*li2[i-1]
#     li3.append(z)
# print(li1)
# print(li2)
# print(li3)


#方法二：函数法
# def mulTwo(a,b):#求2数的乘积
#     return a*b
# def createList(list,start,stop):#创建指定的列表
#     for i in range(start,stop+1):
#         list.append(i)
#     print(list)
#     return list
#
# li1 = []
# li2 = []
# li3 = []
# li1=createList(li1, 1, 4)
# print("li1=",li1)
#
# li2=createList(li2, 2, 5)
# print("li2=",li2)
#
# for i in range(0,4):
#     li3.append(mulTwo(li1[i], li2[i]))
# print("li3=",li3)
#
#
#



########################map()函数的使用
# map(function,iterable,....)可迭代的参数均按照function函数使用
# 由li=[1,2,3,4]====>li=[1, 4, 9, 16]
# 方法一:py2写法，map函数返回的是计算结果,可以直接打印
# li=[1,2,3,4]
# z=map(lambda x:x**2,li)
# print(map(lambda x:x**2,li))
# print(z)

#方法二：py2写法，map函数返回的是计算结果
# def square(x):
#     return x**2
# li=[1,2,3,4]
# z=map(square,li)#这里只能写个函数名，写成这样是是错误的map(square（）,li)
# print(map(square,li))
# print(z)#python2 中要借助中间变量来打印出[1, 4, 9, 16]

#方法二：py3写法，map函数返回的是map对象，是map函数的对象，可以用列表形式展示map对象
# def square(x):            # 计算平方数
#     return x**2
# li=[1,2,3,4]
# z=map(square, li)#计算列表各个元素的平方
# print(list(z)) # 列表形式展示map对象

#方法二：py3写法，map函数返回的是map对象，是map函数的对象，可以用for循环形式展示map对象
# def square(x) :            # 计算平方数
#     return x ** 2
# li=[1,2,3,4]
# li2=[]
# z=map(square, li)#计算列表各个元素的平方
# for i in z:
#     li2.append(i)
#     print(li2)
# print(li2) # 列表形式展示map对象

#总结：py2的时候返回一个可以直接打印的列表，如：print(map(square,li))
#总结：py3的时候返回一个不能直接打印的map函数地址，只能①通过list函数强制转化为列表如：list(map(square, li))
# ②通过for循环每次取出函数对象内的每个数，粘贴到一个空列表中，最后打印这个空列表



#################################lambda函数的使用
# func=lambda x,y,z:x+y+z
# print(func)
# a=func(1,2,3)
# print(a)




###################map函数的使用
#比较三个数的大小，输出最大的，用map函数


#range()函数的使用，
# ①py2:range(3,9)会产生一个列表[3, 4, 5, 6, 7, 8]
#②py3：range(3,9)会产生一个range对象range（3,9）
# li=range(3,9)
# print(type(li))
# print(li)



##################zip() 函数的使用,py2:zip函数返回列表，py3：返回列表对象，需要借助list()函数转化下展示
# a=[1,2,3]
# b=[4,5,6]
# c=[4,5,6,7,8]
# zipped=zip(a,b)
# ww=zip(a,c)
# print ww
# print(zipped)


#打印[('a',97),('b',98),('c',99),....('z',122)]，并输出‘t’对应的ASCII码，用多种方法
#方法1：zip()函数法
# def ASCII(x,y):
#     global ascii
#     ascii=range(x,y)
#     return ascii
#
# def CHAR(asciiX):
#     char=[]
#     for i in asciiX:
#         char.append(chr(i))
#     return char
#
#
# a=ASCII(97,122)
# b=CHAR(ascii)
# print a,b
# zipped=zip(a,b)
# print zipped

#方法2：每次循环产生了一对元组，并将元组对作为元素追加到列表中
# def multi():
#     li1=[]
#     for i in range(97,123):
#         a=(i, chr(i))
#         li1.append(a)
#     print li1
#
# multi()


#求对应元素之积
# li1=[1,3,5,7]
# li2=[2,4,6,8]
# li3=map(lambda a,b:a*b,li1,li2)
# print li3

#求3个等长（整形）列表里的相同位置上的最小值所组成的列表
#方法1：
# import random
# li1=[]
# li2=[]
# li3=[]
# li_min=[]
#
# for i in range(5):#产生3个列表
#     li1.append(random.randint(100,1000))
#     li2.append(random.randint(100, 1000))
#     li3.append(random.randint(100, 1000))
#
# print li1
# print li2
# print li3
#
# for i in range(5):
#     li_min.append(min(li1[i],li2[i],li3[i]))
# print li_min

#用map函数实现zip功能,用map()函数实现以下4段代码的功能
# li1=[1,3,5,7]
# li2=[2,4,6,8]
# li3=zip(li1,li2)
# print li3
# print "######方法1#########"
# li1=[1,3,5,7]
# li2=[2,4,6,8]
# li3=[]
# li3=map(lambda a,b:(a,b),li1,li2)
# print li3



#构造空列表 字典，用函数dict() list()
# li=list()#list()函数里面为空，则构造一个空列表
# dict1=dict()#dict()函数里面为空，则构造一个空列表
# print li,dict1


#构造字典{'a':97，'b':98......'z':122}
# 方法一：普通法
# def multi():
#     li1=[]
#     for i in range(97,123):
#         a=(chr(i),i)
#         li1.append(a)
#     return li1
# a=multi()
# print(a)
# print(dict(a))

#普通法2
# def createList():
#     li1=list()
#     li2=list()
#     li3=list()
#     for i in range(97,123):
#         li1.append(i)
#         li2.append(chr(i))
#     li3=zip(li2,li1)
#     dict3=dict(li3)
#     print(dict3)
# createList()

#方法二：map()函数法
# li1=[]
# li2=[]
# for i in range(97,123):
#     li1.append(i)
#     li2.append(chr(i))
# print li1
# print li2
# li3=[]
# li3=map(lambda a,b:(a,b),li2,li1)
# print dict(li3)



#[{'a':97}，{'b':98}......{'z':122}]===》转化为{'a':97，'b':98......'z':122}
# def createList1():#创建原始列表[{'a':97}，{'b':98}......{'z':122}]
#     global li1
#     li1=list()
#     for i in range(97,123):
#         li1.append({chr(i):i})
#     print "创建原始列表li1=",li1
#
# def  createList2():#取出源列表中每个字典，并将每个字典的key和value组成列表
#     global li2
#     global li3
#     li2=list()
#     li3=list()
#     for i in li1:
#         li2.append(i.keys())
#         li3.append(i.values())
#     print "将列表中的字典的key组成列表li2=", li2
#     print "将列表中的字典的value组成列表li3=",li3
#
# def createList3():  #去除多级列表，只保留字符和数字
#     global li4
#     global li5
#     li4=list()
#     li5=list()
#     for i in li2:
#         li4.append(i[0])
#     print "li2列表去除多级列表得li4=",li4
#     for i in li3:
#         li5.append(i[0])
#     print "li3列表去除多级列表得li5=",li5
#
# createList1()
# createList2()
# createList3()
# li6=list()
# li6=zip(li4,li5)
# print "将li4和li5列表进行zip，得到li6=",li6
# dict1=dict(li6)
# print "dict1=", dict1




#使用函数dict.keys dict.values
# dict1={1:"name",2:"age",3:"sex"}
# print dict1.keys()
# print dict1.values()



#遍历字典
#方法1：循环打印key,value
# dict1={1:"name",2:"age",3:"sex"}
# for key in dict1:
#     # print key
#     print key,dict1[key]

#方法2：dict.items()将字典转化为列表，循环打印
# dict1={1:"name",2:"age",3:"sex"}
# print dict1.items()
# for i in dict1.items():
#     print i,




###########通过字典value得到key
#方法1：循环字典，判断value相等就输出key
# def value_key(dict1,value):
#     for k in dict1:
#         if dict1[k]==value:
#             print k
# dict1={1:"name",2:"age",3:"sex"}
# value_key(dict1,"age")

#方法2：字典转换为列表，判断列表的第二项输出第一项
# def value_key(dict1,value):
#     li=dict1.items()
#     print li
#     for i in li:
#         if i[1]==value:
#             print i[0]
# dict1={1:"name",2:"age",3:"sex"}
# value_key(dict1,"age")


#方法3：输出字典的key,value组成的列表，循环判断value,然后输出对于的index,
# def value_key(dict1,value):
#     keys=dict1.keys()
#     values=dict1.values()
#     print keys,values
#     for value in values:
#         if value=="age":
#             print values.index(value)
#             print keys[values.index(value)]
#
# dict1={1:"name",2:"age",3:"sex"}
# value_key(dict1,"age")

#方法4：交换key value值重新得到字典，再判断key值相等，通过dict[key]找到values
# dict1={1:"name",2:"age",3:"sex"}
# # key=dict1.keys()
# # value=dict1.values()
# # dict2=dict(zip(value,key))#交换key,value组成新的字典
# # print dict2
# # print dict2["age"]#通过key输出对于的value


###########s="aa bb cc dd ee aa ff"
#1)有多少个'aa'?并打印所在位置
#2）可以用几种方法实现，有没有最快的？
#3）设计一个myCount函数，传入s,返回'aa'的个数
#4）设计一个myFind()函数，传入s,返回“aa”所在位置，没有返回-1
#5)以上两个函数有预设值形参start和end

##1)有多少个'aa'?并打印所在位置
#split分割法
# s=" aa aa bb cc dd ee aa ff"
# li=s.split()#用空格分割字符串s,并返回反正单词组成的列表
# num=li.count("aa")#统计单词‘aa’在列表出现的次数
# print li,num
# i=0
# while i<len(li):#循环比较，打印位置
#     if li[i]=='aa':
#         print(i)
#     i+=1
#1)有多少个'aa'?并打印所在位置
#双循环法
# s="aa aa bb cc dd ee aa ff"
# sub='aa'
# x=0
# while x<len(s)-len(sub):
#     y=0
#     num = 0
#     while y<len(sub):
#         if s[x+y]==sub[y]:
#             num+=1
#             if num==len(sub):
#                 print("find 'aa' in ",x)
#         y += 1
#     x+=1
#1)有多少个'aa'?并打印所在位置
#切片法
# s="aa aa bb cc dd ee aa ff"
# sub='aa'
# x=0
# while x<len(s)-len(sub):
#     if s[x:x+len(sub)]==sub:
#         print"find sub in s :",x
#         x+=len(sub)
#     else:
#         x+=1

#3）设计一个myCount函数，传入s,返回'aa'的个数
#循环法
# def myCount(s):
#     sub='aa'
#     x=0
#     while x<len(s)-len(sub):
#         y=0
#         num = 0
#         while y<len(sub):
#             if s[x+y]==sub[y]:
#                 num+=1
#                 if num==len(sub):
#                     print("find 'aa' in ",x)
#             y += 1
#         x+=1
#     return num
#
# s1="aa bb cc dd ee aa ff"
# myCount(s1)

#切片法
# def myCount(s):
#     sub='aa'
#     x=0
#     while x<len(s)-len(sub):
#         if s[x:x+len(sub)]==sub:
#             print"find sub in s :",x
#             x+=len(sub)
#         else:
#             x+=1
# s="aa aa bb cc dd ee aa ff"
# myCount(s)

#设计一个myFind()函数，传入s,返回“aa”所在位置，没有返回-1
#循环法
# def myCount(s):
#     sub='aa'
#     x=0
#     num1=0#统计发现sub次数
#     while x<len(s)-len(sub):
#         y=0
#         num = 0
#         while y<len(sub):
#             if s[x+y]==sub[y]:
#                 num+=1
#                 if num==len(sub):#发现sub,num1加1
#                     num1+=1
#                     print("find 'aa' in ",x)
#             y += 1
#         if x==len(s)-len(sub)-1 and num1==0:
#             return -1
#         x+=1
#     return num1
# s1="aa bb cc dd ee aa ff"
# print(myCount(s1))

#切片法
# def myCount(s):
#     sub='a1a'
#     x=0
#     num=0
#     while x<len(s)-len(sub):
#         if s[x:x+len(sub)]==sub:
#             num+=1
#             print"find sub in s :",x
#             x+=len(sub)
#         else:
#             x+=1
#     if num==0:
#         return -1
# s="aa aa bb cc dd ee aa ff"
# print(myCount(s))

#5)以上两个函数有预设值形参start和end
# s="aa aa bb cc dd ee aa ff"
# sub="aa"
# def myCount(s,sub,start=0,end=len(s)-len(sub)):#
#     x=start
#     num=0
#     while x<end:
#         if s[x:x+len(sub)]==sub:
#             num+=1
#             print"find sub in s :",x
#             x+=len(sub)
#         else:
#             x+=1
#     if num==0:
#         return -1
#
# myCount(s,sub,3,19)

###########判断随机产生的长度为10的整形列表里，有无重复值？
# import random
# def count():
#     li=list()
#     for i in range(10):
#         num=random.randint(0,10)
#         li.append(num)
#     print(li)
#     for i in li:
#         print(i)
#         num2=li.count(i)
#         if num2>=2:
#             print"重复数=",num2



#########随机产生2个列表，li1和li2，合并，并去重;然后进行排序
# li1=[10,9,10,5,0,9,1]
# li2=[1,2,1,10,5,23]
# li3=li1+li2
# li3.sort()
# print(li3)#合并和排序
# for i in li3:
#     if li3.count(i)>1:#循环遍历，看是否有重
#         del li3[li3.index(i)]#通过索引删除重复值得第一个
# print(li3)#去重后输出
# li3.sort()#去重后排序
# print(li3)



########################利用字典实现多分支语句#########################
# def arithmetic(x=1,y=1,operator="+"):
#     result={
#         "+":x+y,
#         "-":x-y,
#         "*":x*y,
#         "/":x/y
#     }
#
#     return result.get(operator)
#
# print(arithmetic(1,2))
# print(arithmetic(1,2,"+"))
# print(arithmetic(y=3,operator="-"))
# print(arithmetic(x=4,operator="+"))
# print(arithmetic(y=3,x=4,operator="-"))
# print(arithmetic(operator="#"))#没有"#"就返回none


#
# def arithmetic(args=[],operator="+"):
#     x=args[0]
#     y=args[1]
#     result={
#         "+":x+y,
#         "-":x-y,
#         "*":x*y,
#         "/":x/y
#     }
#     return result.get(operator,None)
#
#
# print(arithmetic([1,2]))



#################################输入2个索引，找到索引对应的值############################################
# def abc(*t,**d):#元组写在前面，字典写在后面
#     print(t,d)
#     keys=d.keys()
#     values=d.values()
#     for x in t:
#         for key in keys:
#             if x==key:
#                 print(d[key])
#
# abc("one","two",one=1,two=2,three=3)



#########################
# def abc(x,y,z):
#     list1=[x,y,z]#打包：创建一个列表
#     list1.reverse()#逆序排列
#     t=tuple(list1)
#     return t
# a,b,c=abc(1,20,3)
# print(a,b,c)
# print(abc(1,2,3))

###########################通过字典打印
# def abc(**d):
#     print(d)
# abc(a=1,b=2,c=3)


#####################通过元组打印
# def abc(*t):
#     print(t)
# abc(1,2,3)

####################################输入任意个数，求和，数量不限制
#方法1：用元组接收
# def add(*t):
#     sum1=sum(t)
#     print(sum1)
# add(1,2,3,4)

#方法2：用字典接收
# def sumTotal(**d):
#     sum_all=sum(d.values())
#     print( sum_all)
# sumTotal(a=1,b=2,c=300,d=1000)

####################################输入任意个数，求最大值，数量不限制
# def maxOne(**d):
#     max_num=max(d.values())
#     print(max_num)
# maxOne(a=1,b=2,c=300,d=1000)


####################################输入若干个字符串，排序输出，数量不限制
# help(dict.update)
# d=dict(a=1,b=2,c=3)#利用表达式构建字典
# print(d)
# d.update(a1=2,b=1,d=10)#再利用表达式更新字典
# print(d)
# d.update({'a':100,'b':101,'c':102})#利用字典更新字典
# print(d)


#####################################创建集合的方法##############################################
#方法一：{}定义法
# s={'11',123,(1,2,9)}#集合内可以是数字、字符串常量、元组  不能有：列表、字典{[1,2],{1:11,2:22}}
# print(s)
# print(type(s))

#方法一：set()函数法
# s=set()#创建空集合
# print(type(s))
# print(s)
# print("##################")
# li=[1,2]#使用set()函数把list、tuple、dict转化为set
# tu=(1,2)
# dict1={1:11,2:22}
# s1=set(li)
# s2=set(tu)
# s3=set(dict1)#把字典的key值转化为集合
# print(s1,s2,s3)
# print("##################")




#####################################集合的作用之一：去重##############################################
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}#apple orange 都有2个，但是集合只算他出现一次
# print(len(basket))#去重后的长度
# print(basket)
# if "apple" in basket:
#     print("apple in basket")
# else:
#     print("apple not in basket")




#####################################集合的运算：- 、|、 &、  ^、##############################################
#a-b:a集合中去除b：只有a集合有，b集合中无的元素 差集
#a|b：a和b的集合的所有元素 和集
#a&b：a和b集合都有的元素，交集
#a^b：不同时包含于a和b的元素，差集的和
# li1=[1,2,3,4,5]
# li2=[3,4,5,6,7]
# set1=set(li1)#通过列表转化为集合
# set2=set(li2)
# print(set1)
# print(set2)
# print("######################")
# print(set1-set2)#只有set1有，set2中无，差集
# print(set1|set2)#只有set1有，set2中无，去重后的和集
# print(set1&set2)#set1和set2中都有，交集
# print(set1^set2)#仅set1中有的数和仅set2中有的数的和集，(set1-set2)|(set2-set1)差集的和
#

# ##########################################集合的推导
# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)


#####################################添加集合元素
#方法 s.add()函数
# thisset=set(("Google", "Runoob", "Taobao"))#用set()函数将iterable转化为集合
# thisset.add("FaceBook")#添加元组中未有的元素
# print(thisset)
# thisset.add("FaceBook")#添加元组中已有的元素
# print(thisset)


#方法 s.update()函数,函数内部可以是list、tuple、dict
# thisset = set(("Google", "Runoob", "Taobao"))#set()函数将元组转化为集合
# thisset.update({1, 3})#将集合A插入集合B
# print(thisset)
# thisset.update([1, 4], [5, 6])#将2列表插入集合
# print(thisset)

#####################################删除集合元素
#方法一： s.remove() ，存在删除，不存在则报错
# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.remove("Google")#存在则删除
# print(thisset)
# thisset.remove("JingDong")#不存在则报keyError,个人觉得集合就是特殊的字典，删除value后就是key组成的集合，所以报keyError
# print(thisset)

#方法二： s.discard() ，存在删除，不存在也不会报错
# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.discard("Google")#存在则删除
# print(thisset)
# thisset.discard("JingDong")#不存在则报keyError,个人觉得集合就是特殊的字典，删除value后就是key组成的集合，所以报keyError
# print(thisset)


#方法三： s.pop() ，随机删除集合中的一个元素
# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.pop()
# print(thisset)
# thisset.pop()
# print(thisset)



#####################################计算、清空集合元素
# thisset = set(("Google", "Runoob", "Taobao"))
# print(len(thisset))
# thisset.clear()
# print(thisset)




#####################################判断元素是否在集合中
# thisset = set(("Google", "Runoob", "Taobao"))
# if "Runoob" in thisset:
#     print("Runoob in thisset")


#####################################集合的复制、差集
# thisset = set(("Google", "Runoob", "Taobao"))
# thisset.add(4)#添加元素到thisset集合
# print(thisset)
# a=thisset.copy()#copy thisset集合到a集合中
# print(a)
# b=thisset.difference({"Google", "Runoob", "Taobao","www"})#把主集合的有的，辅集合没有的复制出来
# print(b)
# print(thisset)
# thisset.difference_update({'Taobao','Google','Runoob'})
# print(thisset)


#################################判断一个列表里的元素是否都在另一个列表里
#方法一：循环对比法
# li0=[1,2,3,4,5]
# li2=[1,2,5,5]
# n=len(li2)#li2列表的长度
# num=0
# for i in li2:
#     if i in li0:#从li2中抽出一个判断是否在li0中，在就加1，最后判断是否等于li2的长度
#         num+=1
#
# if num==n:
#     print("yes")
# else:
#     print("no")



#方法二：列表转为集合，通过集合的子集函数判断issubset()
# li0=[1,2,3,4,5]
# li2=[1,2,5,5]
# set0=set(li0)
# set2=set(li2)
# a=set2.issubset(set0)#判断集合set2是否为集合set0
# print(a)



###################################################找出两个字典共同的键
#方法一：循环遍历 短列表的数是否在长列表中
# list1=list(range(97,122+1))#产生列表
# list2=list(map(lambda x:chr(x),list1))#用map()函数将a列表转化为b列表
# list3=zip(list2,list1)##（参考1127行字典的创建）zip()函数将2个列表进行组合成可迭代对象，然后字典化输出
# d3=dict(list3)
# print(d3)#产生一个字典
# list4=list(range(97,101))
# list5=list(map(lambda x:chr(x),list4))
# d4=dict(zip(list5,list4))
# print(d4)#产生一个字典
#
# keylist1=d3.keys()#获取字典的key列表
# print(keylist1)
# keylist2=d4.keys()#获取字典的key列表
# print(keylist2)
#
#
# for i in keylist2:
#     if i in keylist1:
#         print(i)


# 方法二：集合的交集找共同的键
# list1=list(range(97,122+1))#产生列表
# list2=list(map(lambda x:chr(x),list1))#用map()函数将a列表转化为b列表
# list3=zip(list2,list1)##（参考1127行字典的创建）zip()函数将2个列表进行组合成可迭代对象，然后字典化输出
# d3=dict(list3)
# print(d3)#产生一个字典
# list4=list(range(97,101))
# list5=list(map(lambda x:chr(x),list4))
# d4=dict(zip(list5,list4))
# print(d4)#产生一个字典
# keylist1=d3.keys()#获取字典的key列表
# print(keylist1)
# keylist2=d4.keys()#获取字典的key列表
# print(keylist2)
#
# set1=set(keylist1)#字典转化为集合
# set2=set(keylist2)#字典转化为集合
# set3=set1.intersection(set2)#2个集合的交集
# set4=set2.intersection(set1)#2个集合的交集
# print(set3)
# print(set4)




###################################################找出两个元组不同的元素
# list1=list(range(97,123))
# list2=list(map(lambda x:chr(x),list1))
# tuple1=tuple(zip(list1,list2))#通过2个列表产生元组
# print(tuple1)
# list3=list(range(97,120))
# list4=list(map(lambda x:chr(x),list3))
# tuple2=tuple(zip(list3,list4))#通过2个列表产生元组
# print(tuple2)
# set1=set(tuple1)#通过元组产生集合
# set2=set(tuple2)
# print("################################")
# print(set1)
# print(set2)
# set3=set1.difference(set2)#返回2个集合的差集
# print(set3)
# set4=set2.symmetric_difference(set1)#返回两个集合中不重复的元素集合。
# print(set4)



###################################################统计某段英文里各个单词出现的次数
# s="abbcacbdaaaa"
# set1=set(s)
# print(set1)#字符串转化为集合，去重后的集合可以知道一个有多少个不重复的字符，然后把这些不重合的字符逐个取出来和原字符串的字母挨个对比，相等就统计出来，
# for i in set1:
#     num=0
#     for j in s:
#         if i == j :
#             num+=1
#     print(i,num)


###################################################合并两列表，要求去重
# list1=list(range(10,21))#产生列表
# list2=list(range(15,26))
# print(list1)
# print(list2)
# list3=list1+list2#列表相加（有重复）
# print(list3)
# set1=set(list3)#列表转化为集合来去重
# print(set1)
# list4=list(set1)#集合转化为列表
# print(list4)


###################################################字典里的键值不同（即唯一）值可相同，请找出相同值得键
#方法一：列表集合化，遍历查找不重复的值
# d={1:"a",2:"a",3:"c",4:"d",5:"e",6:"e",7:"f",8:"d"}#构造字典
# print(d)
# keys=d.keys()#分离key value
# values=d.values()
# print(values)
# set1=set(values)#把value去重，然后统计每个value的个数
# print(set1)
# for i in set1:
#     num=0
#     for j in values:#取出set1中的每个值，挨个和values对比，一旦发现相等，就统计个数，最后输出，
#         if i == j :
#             num+=1
#     if num>1:#发现个数大于1的value,然后在从字典中循环取出，发现相等就打印出来
#         print(i,"有", num,"个")
#         for x in keys:
#             if d[x]==i:
#                 print(i,"所属的key是",x)



#方法一：列表集合化，遍历查找不重复的值
# d={1:"a",2:"a",3:"c",4:"d",5:"e",6:"e",7:"f",8:"d"}#构造字典
# key=d.keys()#key,value分离
# value=d.values()
# print(key)
# print(value)
# value_set=set(value)#value集合化，去重value
# print(value_set)
# for v in value_set:#从不重复的value里取出值挨个和d[key]比较，发现相等立马记下来，
#     num=0
#     li_temp=list()
#     for k in key:
#         if v == d[k]:
#             num+=1
#             li_temp.append(k)
#     print(v,"有",num,"个")
#     print(li_temp)















###################################################去除a列表里属于b列表里的元素()
#第一种情况：两个列表都是无重复数列表
# a=list(range(10,21))
# b=list(range(15,26))
# print(a)
# print(b)
# a_set=set(a)
# b_set=set(b)
# c_set=a_set.intersection(b_set)#找到2集合的交集
# print(c_set)
# li=list()
# for x in a:
#     if x not  in c_set:
#         li.append(x)
# print(li)


#第二种情况：
# a_set=set(a)
# b_set=set(b)
# print(a_set)
# print(b_set)
# c_set=a_set.intersection(b_set)#找到2集合的交集
# print(c_set)
# li=list()
# for x in a:
#     if x not  in c_set:
#         li.append(x)
# print(li)



##################################创建一个文件，并把写入字符串#######
import  os
#创建文件
# context="hello world"
# f=open("hello.txt","w")#open（）函数返回一个文本输入输出包装器（即文件对象）
# f.write(context)
# f.close()



#####################################创建一个文件，并写入字符串，然后判断文件是否关闭，没有关闭最后关闭，关闭了则不作处理
import  os
#创建文件
# context="hello world"
# f=open("hello_1.txt","w")#open（）函数返回一个文本输入输出包装器（即文件对象）
# print(f)
# f.write(context)
# if f.closed :
#     print("文件已经关闭")
# else:
#     print("文件未关闭,正在启动关闭程序")
#     f.close()
#
# a=f.closed
# print("True代表文件已经关闭：",a)






#创建一个文件，并写入字符串，
# ①显示文件的编码类型
# ②显示文件的打开模式
# ③显示文件的名称
# ④显示文件的换行模式
# ⑤返回当前文件的指针
# ⑥返回下一行内容，并将文件的指针移到下一行
# ⑧把字符串序列写入文件
# ⑨打印文件对象
import  os
#创建文件
# context="hello world,\nhello chengpeisheng"
# f=open("hello_1.txt","a")#open（）函数返回一个文本输入输出包装器（即文件对象）
# print("文件编码格式=",f.encoding)#①显示文件的编码类型
# print("文件打开模式=",f.mode)#②显示文件的打开模式
# print("文件名称=",f.name)#③显示文件的名称
# print("文件的换行模式=",f.newlines)#④显示文件的换行模式
# f.write(context)
# f.write('\n')
# li=["111","222","333","444","555","666","777"]
# f.writelines(li)#⑧把字符串序列写入文件
# print("当前文件的指针=",f.tell())#⑤返回文件的指针
# print(f)#⑨打印文件对象
# f.close()





#①创建一个文件
#②写入一个1.1K的字符进去
#③删除1K字节内容
import  os
#创建文件
# context="www hello world,\nhello chengpeisheng"
# f=open("hello_2.txt","a")#open（）函数返回一个文本输入输出包装器（即文件对象）
# f.write(context)
# f.truncate(1)#删除1K大小的字节文件
# f.close()





#逐行读取hello.txt文件
#使用函数readline（）
#
# import os
# f=open("hello.txt","r")#构造一个文件对象
# while True:#使用永真表达式循环读取文件的内容
#     line=f.readline()#读取一行
#     if line:#判断每行是否有内容，有则打印
#         print(line)
#     else:#判断每行是否有内容，没有则跳出循环
#         break
#
# f.close()



#多行读取方式读取hello.txt文件
#使用函数readlines()
# import os
# f=open("hello.txt","r")#构造文件对象，并打开文件对象
# lines=f.readlines()#读取多行，返回值为列表
# print(type(lines))#打印返回的变量类型
# for line in lines:#循环打印列表
#     print(line)
# f.close()#关闭文件对象



#一次性读取方式读取hello.txt文件
#使用函数read(）
# import os
# f=open("hello.txt","r")
# content=f.read()
# print(content)
# f.close()



#每次读取hello.txt文件3个字节内容，并打印当前指针位置
#使用函数read(）
# import os
# f=open("hello.txt","r")
# print("当前指针位置：",f.tell())
# content=f.read(3)
# print(content)
#
# print("当前指针位置：",f.tell())
# content=f.read(3)
# print(content)
#
# print("当前指针位置：",f.tell())
# content=f.read(3)
# print(content)
# f.close()





#使用writelines()方法将列表数据写入到文件中
# import os
# f=open("hello.txt","a+")
# li=["hello world\n","hello china\n","you!\n"]
# f.writelines(li)
# f.close()



#判断文件是否存在，存在则删除
# import os
# f=open("hello.txt","a+")
# f.close()
# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")




#使用read() write()函数实现复制文件A到文件B中
# import os
# src=open("ww.txt","a+")#创建一个file文件对象
# li=["你好\n","世界\n","欢迎你们\n"]
# src.writelines(li)#将列表的字符写入文件
# src.close()#关闭文件
#
# src=open("ww.txt","r")#只读方式打开文件
# dst=open("002.txt","w+")#读写方式打开文件
# dst.write(src.read())#将从src读取到的字符串写入dst文件中
#
# src.close()#关闭文件
# dst.close()#关闭文件



#使用shutil模块copyfile move 进行复制、移动、重命名函数实现复制文件A的复制、移动、重命名
# import os
# import shutil
# file=open("002.txt","w+")#创建file对象
# li=["111\n","222\n","333\n"]
# file.writelines(li)#往文件里写列表
# file.close()
#
# file=open("ww.txt","w+")#创建文件
# li=["@@@\n","!!!\n","$$$\n"]
# file.writelines(li)
# file.close()
#
# shutil.copyfile("002.txt","ww.txt")#将002的文件内容复制到001中，是覆盖式复制
# shutil.move("ww.txt","001_1.txt")#同级目录下的移动就是重命名001-->001_1
# shutil.move("001_1.txt","../")#非同级目录下移动文件
# if os.path.exists("../001_1.txt"):#判断001_1文件是否存在，存在就删除，放置下次移动时产生错误
#     os.remove("../001_1.txt")
#





#①创建文件a.txt b.txt，内容随便
#②列表当前目录的文件列表，
# #③把文件a.txt 重命名为b.txt，
# import os
# file1=open("a.txt","w+")
# file2=open("b.txt","w+")
#
#
# li1=["你好\n","中国\n"]
# li2=["hello\n","china\n"]
# file1.writelines(li1)
# file2.writelines(li2)
# current_diratory=os.listdir(".")
# print(current_diratory)
# file1.close()
# file2.close()
# if 'a.txt' in current_diratory:
#     os.rename("a.txt","a_1.txt")
# if 'b.txt' in current_diratory:
#     os.rename("b.txt","b_1.txt")




#将工作目录下的所有文件列出来
#将所有html文件修改为txt文件
#方法一：

# import os
# #创建三个文件
# file1=open("a.html","w+")
# content=["111\n","222\n","333\n"]
# file1.writelines(content)
# file1.close()
#
# file2=open("b.html","w+")
# file2.writelines(content)
# file2.close()
#
# file3=open("c.html","w+")
# file3.writelines(content)
# file3.close()
# #列出当前目录下的所有文件
# files=os.listdir(".")
# print(files)
# for filename in files:#遍历每个文件，找到后缀名的分割点
#     pos=filename.find(".")
#     if filename[pos:]==".html" :#如果名称中有.html则要源文件的名字改成新文件的名字
#         newname=filename[:pos+1]+".txt"
#         os.rename(filename,newname)



#方法二：
# import os
# import random
# #创建三个文件
# file1=open("a.html","w+")
# content=["111\n","222\n","333\n"]
# file1.writelines(content)
# file1.close()
#
# file2=open("b.html","w+")
# file2.writelines(content)
# file2.close()
#
# file3=open("c.html","w+")
# file3.writelines(content)
# file3.close()
# #列出当前目录下的所有文件
# files=os.listdir(".")
# for filename in files:
#     li=os.path.splitext(filename)
#     if li[1]==".html":
#         num=random.randint(0,100000)
#         newname=li[0]+str(num)+".txt"
#         os.rename(filename,newname)




#方法三：
# import os
# import random
# import glob
# #创建三个文件
# file1=open("a.html","w+")
# content=["111\n","222\n","333\n"]
# file1.writelines(content)
# file1.close()
#
# file2=open("b.html","w+")
# file2.writelines(content)
# file2.close()
#
# file3=open("c.html","w+")
# file3.writelines(content)
# file3.close()
# #列出当前目录下的所有后缀名为.html文件
# files=glob.glob("*.html")
# print(files)
# for filename in files:
#     li=os.path.splitext(filename)
#     print(li)
#     num=random.randint(0,10000)
#     newname=li[0]+str(num)+".txt"
#     os.rename(filename,newname)



#在当前目录下的99.txt文件里找到字符"12"、"hello"字符的个数
#方法 一：
# import os
# file1=open("99.txt","r")
# s=file1.read()#read()返回字符串，readlines()返回列表
# print(s)
# count=s.count("12")
# print("12的个数：",count)
# count=s.count("hello")
# print("hello的个数：",count)
# file1.close()



#在当前目录下的99.txt文件里找到字符"12"、"hello"字符的个数
#方法二
# import re
# file1=open("99.txt","r")
# li1=file1.readlines()#read()返回字符串，readlines()返回列表
# count=0
# for line in li1:
#     li2=re.findall("12",line)#在字符串line中找12，把找到的所有12 组成一个列表
#     if len(li2)>0:#如果每行找到字符"12"的个数大于0，则把找到的个数累计相加
#         count=count+len(li2)
# print(li1)#打印源文本
# print(count)#打印个数
# file1.close()



#在当前目录下的99.txt文件里替换字符"hello"为"hey"
# file1=open("99.txt","r")
# file2=open("cps.txt","w+")
# for s in file1.readlines():
#     file2.writelines(s.replace("hello","hey"))
# file1.close()
# file2.close()
# #如果在调试窗口显示出来，必须先关闭文件，在打开，否则上述操作没保存下来，file2为空了。
# file2=open("cps.txt","r")
# str=file2.read()
# print(str)



#############################
###目录的相关操作
# import os
# import random
# now_path=os.getcwd()#获取当前 工作路径
# print("修改前工作路径为：",now_path)
#
# name=str(random.randrange(1,10000))
# os.mkdir(name)#在当前工作目录创建一个name文件夹
# os.rmdir(name)
#
# os.makedirs("name1/name2")
# os.removedirs("name1/name2")
#
# print("列举目录下的文件：",os.listdir("D:\python_project/006"))#D:\python_project\006\ww\001写法为：D:\python_project/006/ww/ww
# os.chdir("D:\python_project/006/ww")#切换工作路径为   D:\python_project/006/ww
# print("修改后工作路径为",os.getcwd())#获取当前 工作路径
# print(list(os.walk(".")))



#将1-1000000分行写进某.txt文件
# import random#导入随机数模块
# name=str(random.randint(1,10000))+".txt"#文件名为随机数，保证不重复
# print("name=",name)#打印文件名
# file=open(name,"w+")#读写的方式打开文件
# li=list(range(1,1000))#产生列表
# print("li=",li)#打印列表
# for i in li:#从列表中逐个取出每个列表元素，然后进行字符串化，最后再加上换行操作，写入到文件逐行里
#     file.writelines(str(i)+"\n")
# file.close()



#拷贝a.txt文件内容到b.txt文件里
#方法一：将整个列表写入到文件中（列表中的内容必须是字符串，readlines(str)）
# li=list(range(1,100))#创建一个列表
# print("li=",li)#打印列表
# file=open("a.txt","w+")#创建一个文件，并把列表中的每个元素往里面写
# for s in li:
#     file.writelines(str(s)+"\n")
# file.close()#保存+关闭文件，
# file=open("a.txt","r")#重新打开已经保存的文件
# print("file=",file.read())#把文件全部内容再次读取出来，，并打印
# file.close()
# print("即将把a.txt内容写入到b.txt文件中")
# print("############################")
# file2=open("b.txt","w+")
# file=open("a.txt","r")
# file2.writelines(file.readlines())#将读出的字符列表一起写入
##file2.write(file.read())#同上面作用，将所读取到的字符串内容全部写入文件内
# print("写入完成")
# file.close()
# file2.close()




#方法二：将文件a.txt内容逐个写入到文件b.txt中，
# li=list(range(1,100))#创建一个列表
# print("li=",li)#打印列表
# file=open("a.txt","w+")#创建一个文件，并把列表中的每个元素往里面写
# for s in li:
#     file.writelines(str(s)+"\n")
# file.close()#保存+关闭文件，
# file=open("a.txt","r")#重新打开已经保存的文件
# print("file=",file.read())#把文件全部内容再次读取出来，，并打印
# file.close()
# print("即将把a.txt内容写入到b.txt文件中")
# print("############################")
# file2=open("b.txt","w+")
# file=open("a.txt","r")
# for s in file.readlines():#从a.txt文件中把内容中读取内容列表（每行已经字符串化了），然后逐行把列表中的字符串写入到b.txt中
#     file2.writelines(s)
# print("写入完成")
# file.close()
# file2.close()




#将a.txt文件的内容逆序拷贝到b.txt文件里
# li=list(range(1,100))#创建一个列表
# print("li=",li)#打印列表
# file=open("a.txt","w+")#创建一个文件，并把列表中的每个元素往里面写
# for s in li:
#     file.writelines(str(s)+"\n")
# file.close()#保存+关闭文件，
# file=open("a.txt","r")#重新打开已经保存的文件
# print("file=",file.read())#把文件全部内容再次读取出来，，并打印
# file.close()
# print("即将把a.txt内容写入到b.txt文件中")
# print("############################")
# file2=open("b.txt","w+")
# file=open("a.txt","r")
# for s in file.readlines():#从a.txt文件中把内容中读取内容列表（每行已经字符串化了），然后逐行把列表中的字符串写入到b.txt中
#     file2.writelines(s)
# print("写入完成")
# file.close()
# file2.close()




#统计某单词在某文件里出现的次数
# a=open("a.txt","w+")#打开文件并清空原文件
# a.write("hi everyone! this is Sunday  today! It`s hot day! I write one emaill to my computer!")
# a.close()
# a=open("a.txt","r")#只读打开文件
# count=0#统计字符个数的变量
# for s in a.read():
#     if s=="s":#统计字符"s"的个数
#         count=count+1
# print(count)
# a.close()



#将数据写入到文件a.txt ,展示效果如下
# 0001    hi0001   'f'
# 0002    hi0002   'm'
# 0003    hi0003   'f'
#   ...
# 9999    hi9999   'm'

#方法一：通过三个临时文件存储，再读取出来给一个文件
# c=open("xxxx.txt","w+")#创建一个文件
# temp=list(range(1,10))#产生1-9的列表
# for x in temp:#将列表中的每个数字转化为字符串并加上"000"和"\n"
#     x="000"+str(x)+"\n"
#     c.write(x)#将转化后的字符串加入到文件中，构成了0001-0009
#
# temp=list(range(10,100))#构造0010-0099
# for x in temp:
#     x="00"+str(x)+"\n"
#     c.write(x)
#
# temp=list(range(100,1000))#构造0100-0999
# for x in temp:
#     x="0"+str(x)+"\n"
#     c.write(x)
#
# temp=list(range(1000,10000))#构造1000-9999
# for x in temp:
#     x=str(x)+"\n"
#     c.write(x)
# c.close()
#
# print("0000-9999创建完毕")
# print("###################")
#
# d=open("hixxxx.txt","w+")#同上思路
# temp=list(range(1,10))
# for x in temp:
#     x="hi"+"000"+str(x)+"\n"
#     d.write(x)
#
# temp=list(range(10,100))
# for x in temp:
#     x="hi"+"00"+str(x)+"\n"
#     d.write(x)
#
# temp=list(range(100,1000))
# for x in temp:
#     x="hi"+"0"+str(x)+"\n"
#     d.write(x)
#
# temp=list(range(1000,10000))
# for x in temp:
#     x="hi"+str(x)+"\n"
#     d.write(x)
# d.close()
#
# print("hi0000-hi9999创建完毕")
# print("###################")
#
# e=open("fm.txt","w+")
# temp=list(range(1,10000))
# for x in temp:
#     if int(x%2)==0:
#         e.write("m"+"\n")
#     else:
#         e.write("f"+"\n")
# e.close()
#
# print("f-m创建完毕")
# print("###################")
#
#
# c=open("xxxx.txt","r")#
# d=open("hixxxx.txt","r")#
# e=open("fm.txt","r")
# f=open("cycle.txt","w+")
# num=list(range(1,10000))
# for x in num:
#     f.write(c.readline()+d.readline()+e.readline())
#
# f.close()
# e.close()
# d.close()
# c.close()


#方法二：直接将三个循环数写入到文件中
# c=open("cycle.txt","w+")#创建一个文件
# temp=list(range(1,10))#产生1-9的列表
# for x in temp:#将列表中的每个数字转化为字符串并加上"000"和"\n"
#     if x%2==0:
#         x = "000" + str(x) + " " + "hi" + "000" + str(x) +" "+"m"+"\n"
#         c.write(x)  # 将转化后的字符串加入到文件中
#     else:
#         x = "000" + str(x) + " " + "hi" + "000" + str(x) +" " +"f"+"\n"
#         c.write(x) # 将转化后的字符串加入到文件中
#
# temp=list(range(10,100))#产生10-99的列表
# for x in temp:#将列表中的每个数字转化为字符串并加上"00"和"\n"
#     if x%2==0:
#         x = "00" + str(x) + " " + "hi" + "00" + str(x) +" "+"m"+"\n"
#         c.write(x)  # 将转化后的字符串加入到文件中
#     else:
#         x = "00" + str(x) + " " + "hi" + "00" + str(x) +" "+ "f"+"\n"
#         c.write(x) # 将转化后的字符串加入到文件中
#
# temp=list(range(100,1000))#产生100-999的列表
# for x in temp:#将列表中的每个数字转化为字符串并加上"0"和"\n"
#     if x%2==0:
#         x = "0" + str(x) + " " + "hi" + "0" + str(x) +" "+"m"+"\n"
#         c.write(x)  # 将转化后的字符串加入到文件中
#     else:
#         x = "0" + str(x) + " " + "hi" + "0" + str(x) +" "+ "f"+"\n"
#         c.write(x) # 将转化后的字符串加入到文件中
#
# temp=list(range(1000,10000))#产生1000-9999的列表
# for x in temp:#将列表中的每个数字转化为字符串并加上"\n"
#     if x%2==0:
#         x = str(x) + " " + "hi"+ str(x) +" "+"m"+"\n"
#         c.write(x)  # 将转化后的字符串加入到文件中
#     else:
#         x =str(x) + " " + "hi"+str(x) +" "+ "f"+"\n"
#         c.write(x) # 将转化后的字符串加入到文件中
# c.close()


#######################################################
# 一：定义一个学生类。有下面的类属性：
#
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
#
# 类方法：
#
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
#
#
# 写好类以后，可以定义2个同学测试下:
#
# zm = student('zhangming',20,[69,88,100])
# 返回结果：
# zhangming
# 20
# 100
#
# lq = student('liqiang',23,[82,60,99])
#
# 返回结果：
# liqiang
# 23
# 99
##############################################################
#方法一：直接调用初始化函数的实例属性self.name self.age self.course
# class Students():#类名中要self？python2中是写object,python3中不写任何东西，除非要继承父类（父类要在子类前面写不？）
#     def __init__(self,name,age,course):#类中必须要初始化构造函数吗？
#         print("初始化开始")
#         self.name=name #name可以被对象调用
#         self.age=age #age可以被对象调用
#         self.course=course #course可以被对象调用
#
# zm=Students("zhangming" , 20 , [69 , 88 ,100])
# print(zm.name)#__init__函数中必须要self.name否则name不被对象调用
# print(zm.age)
# print(zm.course)
#
# lq=Students("liqiang", 23, [82, 60, 99])
# print(zm.name)
# print(zm.age)
# print(zm.course)

#方法二：通过类中的其他方法返回self.name self.age self.course
# class Students():#类名中要self？python2中是写object,python3中不写任何东西，除非要继承父类（父类要在子类前面写不？）
#     def __init__(self,name,age,course):#类中必须要初始化构造函数，且如果类需传递变量，必须要在__init__方法中初始化下，否则类就无法传递参数，就是无参数的类
#         print("初始化开始")
#         self.name=name #name可以被对象调用
#         self.age=age #age可以被对象调用
#         self.course=course #course可以被对象调用
#
#     def getName(self):
#         return self.name
#         pass #pass代表方法结束，可以不写，如果是空方法一定要写个pass,否则会因为没有操作报IndentationError
#
#
#     def getAge(self):
#         return self.age
#         pass
#
#     def getCourse(self):
#         return self.course
#         pass
#
# zm=Students("zhangming" , 20 , [69 , 88 ,100])#每次实例化都要调用__init__方法
# print(zm.getName())#__init__函数中必须要self.name否则name不被对象调用
# print(zm.getAge())#通过对象调用方法，
# print(zm.getCourse())
#
# lq=Students("liqiang", 23, [82, 60, 99])
# print(lq.getName())#__init__函数中必须要self.name否则name不被对象调用
# print(lq.getAge())
# print(lq.getCourse())


######################################################################
# 二：定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

# class Dict():
#     def __init__(self,dict):#构造函数，然后初始化dict,
#         self.dict=dict#定义实例属性dict,方便对象和类内方法使用，使用时要用self.dict否则报缩进错误
#
#     def del_key(self,key):
#         self.dict.pop(key,"key不存在，请重新输出存在的key值")
#         print("删除后的dict=",self.dict)
#
#     def get_dict(self,key):
#         if key in self.dict:
#             print(key,":",self.dict[key])#返回键值对
#         else:
#             print("not found %s in dict"%(key))
#
#     def get_key(self):
#         print(self.dict.keys())
#
#     def update_dict(self,dict1,dict2,dict3):
#         dict3.update(dict1)
#         dict3.update(dict2)
#         print("dict3=",dict3)
#         print(dict3.values())
#
# dict_x={"1":"a","2":"b","3":"c"}
# dict_x0={"3":"d","4":"e","5":"f"}
# dict_x1={"6":"g","7":"h","8":"i"}
# dict_x2=dict()#创建空字典
# zd=Dict(dict_x)
# zd.del_key("1")
# zd.get_dict("20")
# zd.get_key()
# zd.update_dict(dict_x0,dict_x1,dict_x2)



##############################################################################
# 定义一个列表的操作类：Listinfo
# 包括的方法:
# 1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
# 2 获取列表元素前num位：get_key(num) [num:整数类型]
# 3 列表合并：update_list(list)	  [list:列表类型]
# 4 删除并且返回最后一个元素：del_key()
# list_info = Listinfo([44,222,111,333,454,'sss','333'])
##############################################################################
# class Listinfo():
#     def __int__(self,list_x):#默认为列表添加一个整数10
#         self.list_x = list_x
#         print("初始化........")
#         print("添加前的列表=    ",self.list_x)
#
#     def add_key(self,value):
#         self.list_x.append(value)
#         print("添加 %s 后的列表="%(value),self.list_x)
#
#     def get_key(self,num):
#         print("获取列表前%s位"%(num),self.list_x[:num])
#
#     def update_list(self,list_x2):
#         self.list_x.extend(list_x2)
#         print("合并后的列表=",self.list_x)
#
#     def del_key(self):
#         self.list_x.pop()
#         print("删除列表最后一位之后=",self.list_x)
#
# li0 = [44,222,111,333,454,"sss","333"]
# li_0=[11,22,33,44,55,"nihao","985"]
# li1=Listinfo()#构造对象
# li1.__int__(li0)#初始化列表
# li1.add_key(10)#给列表增加一个数字10
# li1.get_key(4)#获取列表前4位数
# li4=li1.update_list(li_0)#合并列表
# li1.del_key()#删除列表中最后一个值



################################################################################
# 定义一个集合的操作类：Setinfo
# # 包括的方法:
# # 1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
# # 2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
# # 3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
# # 4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
# # set_info =  Setinfo(你要操作的集合)
# s.add( x )
# s.intersection()
# s.union()
# s.difference()
# class Setinfo():
#
#     def __int__(self,collect_0):
#         self.collect_0 = collect_0
#
#     def add_setinfo(self,keyname):# 1 集合元素添加
#         self.collect_0.add(keyname)
#         print("2集合相加=",self.collect_0)
#
#     def get_intersection(self,unioninfo): # 2 集合的交集
#         print("2个集合%s%s"%(self.collect_0,unioninfo),"的交集",self.collect_0.intersection(unioninfo))
#
#     def get_union(self,unioninfo):# 集合的并集
#         print("2个集合%s%s"%(self.collect_0,unioninfo),"的并集",self.collect_0.union(unioninfo))
#
#     def del_difference(self,unioninfo):# 4 集合的差集
#         print("2个集合%s%s"%(self.collect_0,unioninfo),"的差集",self.collect_0.difference(unioninfo))
#
# s1=5
# s0={1,2,3}
# s2={2,3,5}
# s3={2,3,9}
# collect_1=Setinfo()#类实例化
# collect_1.__int__(s0)#初始化一个类a
# collect_1.add_setinfo(s1)#将类b加上类a
# collect_1.get_intersection(s2)
# collect_1.get_union(s2)
# collect_1.del_difference(s2)




##########################################################################################
#用类实现一个计算器功能
# class Calculator:
#
#     def __init__(self,result=0):#给构造函数的实例属性一个初始值0，否则程序不知道result的类型，
#         self.result=result
#
#     def addition(self,number1,number2):
#         self.result=number1+number2
#         print("%s+%s="%(number1,number2),self.result)
#
#     def subtraction(self,number1,number2):
#         self.result=number1-number2
#         print("%s-%s="%(number1,number2),self.result)
#
#     def multiplication(self,number1,number2):
#         self.result=number1*number2
#         print("%s*%s="%(number1,number2),self.result)
#
#     def division(self,number1,number2):
#         self.result=number1/number2
#         print("%s/%s="%(number1,number2),self.result)
#
#
# calculator=Calculator()#类的实例化，对象calculator中的result属性已经初始化，方便后边的对象方法调用
# calculator.addition(2,2)#对象的addition函数调用加法方法（加法函数）
# calculator.subtraction(3,2)#对象的subtraction函数调用减法方法（减法函数）
# calculator.multiplication(4,2)#对象的multiplication函数调用乘法方法（乘法函数）
# calculator.division(4,2)#对象的division函数调用除法方法（除法函数）





#展示基本的异常使用方法
# try:
#     print("12"+12)#这段代码是错误的，下面一行代码不运行了，直接跳到except执行
#     print("可能出错的代码")
#
# except:
#     print("出错时运行此段代码")
# else:
#     print("没出错时运行这个代码")
# finally:
#     print("对错我不管，这个代码必须运行")


#拦截列表索引溢出问题
# li=list(range(1,6))
# n=45
# try:
#     print(li[n])
# except:
#     print("list index out of range")
# else:
#     print(li[n])
# finally:
#     print("请输出所有列表元素")

#输入一个网址，如果网址非法就拦截下来提示用户重新输入网址，如果网址正常就打开网址
# from urllib import request
# url="https://www.csdn.net/"
# try:
#     d=request.urlopen(url)
#     print("网址是对的")
# except:
#     print("url不对，请重新输入网址")
# else:
#     d=request.urlopen(url)
# finally:
#     request.urlcleanup()


# from first import * # *代表引进__all__包含的方法，不一定是first模块里的所有方法，要看__all__怎么定义
# gg()
# yy()
# hh()

# import  first
# print(first.__all__)



# import sys
# try:
#     a=3
#     assert a>4 #断言出现了异常
# except:
#     print("a<=4")#断言异常了，就代码a<=4




# import sys
# try:
#     a=3
#     assert a>4 #断言出现了异常
# except:
#     exc=sys.exc_info()
#     print(exc)#断言异常了，就代码a<=4




####在当前路径下建个sendlog.txt文件，然后将日志往里面写入
# import logging
# logger=logging.getLogger()#调用getLogger函数
# hdlr=logging.FileHandler("sendlog.txt")#FileHandler可以往文件sendlog.txt中写带格式的日志
# formater=logging.Formatter("%(asctime)s %(levelname)s %(message)s")#Formatter 类的实例化，将日志写入到text文件
# hdlr.setFormatter(formater)
# logger.addHandler(hdlr)
# logger.setLevel(logging.NOTSET)
# logger.debug("this is a debug message")

########同上
# import logging
# hdlr = logging.FileHandler("sendlog.txt")  # FileHandler可以往文件sendlog.txt中写带格式的日志
# formater = logging.Formatter("%(asctime)s %(levelname)s %(message)s")  # Formatter 类的实例化，将日志写入到text文件

# hdlr.setFormatter(formater)  # 往sendlog.txt文件里格式化填写
# logging.getLogger().addHandler(hdlr)  # 填写的handle
# logging.getLogger().setLevel(logging.NOTSET)  # 填写登记
# logging.getLogger().debug("this is a debug message")
# logging.getLogger().error("this is error")  # 输出debug信息
# logging.getLogger().critical("this is critical!")  # 输出debug信息
# logging.getLogger().exception("this is exception")#





# with 语句的使用可以不使用close()函数，因为它已经启用了关闭文档的命令了
#普通写入
# d=open("cps.txt","w+")
# d.write("不忘初心，牢记使命")
# d.close()#没有它随便不报错，但是文件一直是处于打开的状态，其余程序无法写入了

#with方法写入，不需使用close(),代码块结束后就关闭了文件了
# with 语句的使用可以不使用close()函数，因为它已经启用了关闭文档的命令了
# with open("cps.txt","w+") as d :
#     d.write("初心，使命,")
#     pass





#类的继承，子类使用父类方法
# class Fruit:
#     def __init__(self,color):
#         self.color=color
#         print("fruit^s color:%s"%self.color)
#
#     def grow(self):
#         print("grow...")
#
#
# class Apple(Fruit):
#     def __init__(self,color):
#         Fruit.__init__(self,color)#调用Fruit类的__init__方法，
#         print("apple^s color: %s"%self.color)
#
# class Banana(Fruit):
#     def __init__(self,color):
#         Fruit.__init__(self,color)#调用
#         print("banana^s color :%s "%self.color)
#     def grow(self):
#         print("banana grow ...")
#
#
# if __name__ ==  "__main__":
#     apple = Apple("red")
#     apple.grow()#apple类没有grow方法，通过子类调用父类的方法
#     banana = Banana("yellow")
#     banana.grow()#banana类有grow方法，直接通过子类直接调用，总结一句话：自己有，直接调用，自己没有，也可以自己调（内部实现是通过父类调）



#异常的使用，多except情况使用；except 错误类型 ：
# try :
#     open("cps@.txt","r")
#     print("cps@.txt 文件存在")
# except FileNotFoundError :#捕获FileNotFoundError异常，进行补充说明
#     print("cps@.txt 文件不存在")
# except :
#     print("非文件不存在异常")


#捕获0为除数的情况
# try :
#     x=10
#     y=3
#     z=y/x
# except ZeroDivisionError :#捕获0为除数的情况，并进行中文说明
#     print("x 不能被 y 整除")
#
# else:# 没有异常时，计算结果
#     print("y/x=%s"%z)



#嵌套try 使用
# try :#外部try
#     s = "hello"
#     # print(s[10])
#     try:#内部try有2个异常分支：TypeError、IndexError
#
#         print (s[0]-s[1])#异常后的语句块不再执行
#         print(s[0] + s[1])
#     except TypeError:
#         print("字符串不支持减法")
#     except IndexError:
#         print("字符串索引超出范围")
# except :#外部try异常
#     print("外部try异常")

#
# try :
#     s=None
#     if s is None:
#         print("s是 空变量")
#         raise NameError #手动抛出NameError异常，后面的代码块不再运行，直接匹配except，然后打印出提示语： 空对象没有长度
#     print("1")
#     print(len(s))
# except NameError:
#     print("空对象没有长度")




