########################################################################################################################
#获取项目绝对路径
########################################################################################################################
import os
def get_Path():
    #方法一：os.path.splite()方法
    # os.path.realpath获取__file__(当前文件)的带文件名的绝对路径，以字符串格式显示，然后用os.path.realpath把绝对路径分割，分割的
    #界限是最后一个"\"  产生的结果是元组，元组中有2个元素，分别是文件的绝对路径和文件名称。例如：带文件名的绝对路径是：
    #D:\python_code\复习\auto_interface_test\getpathInfo.py ,用os.path.realpath函数分割后就是（"D:\python_code\复习\auto_interface_test","getpathInfo.py"）
    # path = os.path.split(os.path.realpath(__file__))[0]

    #方法二：字符串切片
    path=os.path.realpath(__file__)[:-15]#分割思想： 除掉\auto_interface_test就是项目的绝对路径
    return path#str格式字符串

if __name__ == "__main__":
    print("测试获取路径方法ok,路径为：",get_Path())



