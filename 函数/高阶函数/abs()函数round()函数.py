# abs()
# 函数可以完成对数字求绝对值
print(abs(-10))

# round()
# 函数可以完成对数的四舍五入计算
print(round(1.2))
print(round(1.8))
print('------------------------------')

#需求：任意两个数字，先进行数字处理（绝对值或四舍五入）再求和计算
# 1.写法一
def add_num(a,b):
    #绝对值
    return abs(a)+abs(b)
result = add_num(-1.1,1.9)
print(result)
print('------------------------------')
# 2.写法二
def sum_num(a,b,f):
    #绝对值
    return f(a)+f(b)
result1 = sum_num(-1.1,1.9,abs)
print(result1)
result2 = sum_num(1.1,1.9,round)
print(result2)