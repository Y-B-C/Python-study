# 1.准备列表数据
list1 = [1,2,3,4,5]

# 2.准备2次方计算的函数
def func(x):
    return x ** 2

# 3.调用map
result = map(func,list1)


# 4.验收成果
print(result)           #   打印的是迭代器
print(list(result))     #   [1, 4, 9, 16, 25]