
def testA():
    a = 10
    print(a)   # 函数内部访问，可以访问到a变量
testA()

# print(a)     #报错：函数外部无法访问   a是一个局部变量

#    全局变量---->函数体内、外都能生效
b= 100

def testA():
    print(b)
testA()
print(b)