#coding:utf-8
#读取Excel的方法
import os
from auto_test_frame.getpathInfo import get_Path
from xlrd import open_workbook

#获取项目所在的绝对路径
path = get_Path()#项目路径：D:\python_project\auto_test_frame

class ReadExcel():
    def get_xls(self,xls_name,sheet_name):
        cls=[]
        xlsPath = os.path.join(path,"testFile\case",xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows#获取sheet页的数据行数
        for i in range(nrows):#根据行数循环，将所有行都进行搜索
            if sheet.row_values(i)[0]!="case_name":#获取sheet页中第i行的第一个数，如果不为case_name则将值传给cls列表
                cls.append(sheet.row_values(i))
        return cls#返回测试用例总信息



if __name__ == "__main__":
    readExcel=ReadExcel()#类的实例化，构造对象readExcel
    print(readExcel.get_xls("userCase.xlsx","login"))#读取sheet=login那页的所有值
    print(readExcel.get_xls("userCase.xlsx","login")[0][1])#读取sheet=login那页的[0][1]值
    print(readExcel.get_xls("userCase.xlsx","login")[1][2])#读取sheet=login那页的[1][2]值