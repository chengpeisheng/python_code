########################################################################################################################
#读取Excel的方法
########################################################################################################################
import os
from auto_interface_test import getpathInfo
from xlrd import open_workbook

path=getpathInfo.get_Path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):#构造读取表格用例的方法
        cls=[]
        xls_path=os.path.join(path,"testFile","case",xls_name)#获取userCase.xlsx的绝对路径
        file=open_workbook(xls_path)#打开指定表格
        sheet=file.sheet_by_name(sheet_name)#打开指定sheet
        nrows=sheet.nrows#获取sheet行数
        for i in range(nrows):#遍历每行
            if sheet.row_values(i)[0]!= u"case_name":#如果每行的的[0]元素不是case_name就是我们要的数据，将数据粘贴到列表中
                cls.append(sheet.row_values(i))#
        return cls

if __name__ == "__main__":
    excel=readExcel()#
    print(excel.get_xls("userCase.xlsx","login"))



