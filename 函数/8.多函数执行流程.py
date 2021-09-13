num = 0
def test1():
    global num
    num = 100

def test2():
    print(num)

print(num)   #  0    因为修改的函数没有执行
test2()      #  0    test1没有执行
test1()
test2()      #  100   先调用了函数 test1
print(num)   #  100   调用了函数   test1
print('------------------------------')
#   返回值作为参数传递
def test3():
    return 50
def test4(num2):
    print(num2)

result = test3()
# print(result)
test4(result)