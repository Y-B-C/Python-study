
#如果一个模块文件中有__all__变量，当前from xxx import *导入时，只能导入这个列表中的元素
__all__ = ['testA']

def testA():
    print('testA')

def testB():
    print('testB')

