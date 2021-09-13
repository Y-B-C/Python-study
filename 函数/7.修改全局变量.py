b= 100

def testA():
    print(b)

def testB():
    b= 200   #定义的是局部变量
    print(b)
testA()
testB()

print(b)   #   b的值没有变，还是一百
print('-----------------------')

a= 100

def testC():
    print(a)

def testD():
    global a  # 声明a是全局变量
    a = 200
    print(a)
testC()
testD()
print(a)
