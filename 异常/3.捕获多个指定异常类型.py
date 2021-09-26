try:
    print(1/0)
except(NameError,ZeroDivisionError):
    print('有错误')


print('-------------------------------')
#        捕获异常描述信息
try:
    print(1/0)
except(NameError,ZeroDivisionError) as result:
    print(result)
