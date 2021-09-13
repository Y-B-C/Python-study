# 引用是否可以当做实参 ----> 引用可以当实参使用
def test1(a):
    print(a)
    print(id(a))

    a +=a
    print(a)

    print(id(a))
b = 100
test1(b)
print('-------------------')
c =[11,22]
test1(c)