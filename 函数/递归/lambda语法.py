# 可以使用 lambda 简化代码
# 1.函数
def fn1():
    return 100
result = fn1()
print(result)

#2.lambda
#lambda 参数列表：表达式
fn2 = lambda :100
print(fn2)    # lambda内存地址
print(fn2())  # 100

print('-------------------------')
# 1.函数
def add(a,b):
    return a + b
result = add(1,2)
print(result)

#2.lambda
#lambda 参数列表：表达式
fn3 = lambda a,b : a + b
print(fn3(1,2))