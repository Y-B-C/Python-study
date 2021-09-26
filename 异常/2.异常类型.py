"""
try:
    可能发生错误的代码
except 异常类型:
    如果捕获到该异常类型执行的代码

"""
#需求：尝试执行打印num,捕获异常类型NameError,如果捕获到这个异常类型，执行打印：有错误
try:
    print(num)
except NameError:
    print('有错误')







