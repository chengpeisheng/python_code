#coding:UTF-8
#python3编译环境要求被调模块放置的位置：
# ①与主调用模块在同一文件里;最好不要这样，因为这种放置方法初
# 次调用函数时不会有函数智能提示语，用起来苦逼；只有调用过的函数才会有,
# 而且提示语的颜色还是灰白色，不是系统的正宗颜色

# ②在安装包所在的Lib库，例如 E:\Install_here\python3\Lib
# ③放在E:\Install_here\python2\Lib\site-packages文件里
import mathFunc
mathFunc
print(z)