import unittest

def div(a,b):
    if b==0:
        return "0不能作为除数"
    else:
        return a/b

class Test_div(unittest.TestCase):
    def setUp(self):
        print("用例前准备")

    def tearDown(self):
        print("用例后准备")

    def test_1div1(self):
        self.assertEqual(1/1,div(1,1),"1/1！=1，除法异常")

    def test_3div4(self):
        self.assertEqual(3/4,div(3,4),"3/4!=0，除法异常")

    def test_3div0(self):
        self.assertEqual("0不能作为除数",div(3,0),"3/0有结果，除法异常")

if __name__ == "__main__":
    unittest.main()

