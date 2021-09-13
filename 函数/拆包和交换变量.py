#    拆 包
#    交换变量值
#    拆 包：元组
def return_num():
    return 100,200,300

num1,num2,num3 = return_num()
print(num1)
print(num2)
print(num3)

#    拆 包:   字典
dict1 = {'name':'TOM','age':18}
a,b= dict1
print(a)
print(b)

print(dict1[a])
print(dict1[b])

print('----------------------------------------')
#       交换 a  b 数据
# 方法一
c = 20
d = 10

# 赋值
e = 0
e = c
c = d
b = c
print(a)
print(b)
print('----------------------------')
# 方法二
a,b = 1,2
print(a)
print(b)
a,b = b,a
print(a)
print(b)
