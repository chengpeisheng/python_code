#coding:utf-8
#python unittest框架自带assert
import unittest

def div(a,b):#除法函数，函数和方法的区别在于有没有self
    return a/b

class Test_div(unittest.TestCase):
    def setUp(self):#初始化方法,函数和方法的区别在于有没有self
        print("用例初始化完毕")

    def test_01(self):
        result=1/1
        self.assertEqual(div(1,1),result)

    def test_02(self):
        result=3/4
        self.assertEqual(div(3,4),result)

    def test_03(self):
        self.assertRaises(ZeroDivisionError,div(3,0),)


    def tearDown(self):
        print("用例执行完毕")


if __name__ =="__main__":
    unittest.main()




