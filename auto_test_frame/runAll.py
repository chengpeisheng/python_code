#coding:utf-8
#开始执行接口自动化，项目工程部署完毕后直接运行该文件即可

import auto_test_frame.common.configEmail as configEmail
import auto_test_frame.getpathInfo as getpathInfo
import os
import auto_test_frame.readConfig as readConfig


send_email = configEmail.Send_Email()#构造send_email对象，邮箱终端有三种：QQ、163、Outlook
path = getpathInfo.get_Path()#获取项目路径 D:\python_project\auto_test_frame
report_path = os.path.join(path,"result")#获取项目报告的路径  D:\python_project\auto_test_frame\result
on_off = readConfig.ReadConfig().get_email("on_off")#获取on_off值

class AllTest():
    def __init__(self):#初始化参数和数据
        global resultPath
        resultPath = os.path.join(report_path,"report.html")#获取项目报告精确的路径D:\python_project\auto_test_frame\result\report.html
        self.caseListFile = os.path.join(path,"caselist.txt")#获取caselist.txt文件路径 D:\python_project\auto_test_frame\caselist.txt
        self.caseFile = os.path.join(path,"testCase")#获取测试用例
        self.caseList = []#即将执行的用例

    def set_case_list(self):
        '''
        读取caselist.txt中的用例名称，并添加到caselist元素组
        :return:
        '''
        fb=open(self.caseListFile,"rb")#由于castlist.txt文件里面有中文，所以要有二进制方式打开文件
        for value in fb.readlines():
            data = str(value)
            if data != "" and not data.startswith("#"):#如果data非空，且没有注释掉
                self.caseList.append(data.replace("\n",""))#将换行符替换为空，保证用例名不是test01case\n 而是test01case
        fb.close()

    def set_case_suite(self):
        '''

        :return:
        '''


    def run(self):
        pass
if __name__ == "__main__":
    AllTest().set_case_list()
    # AllTest().run()