# 查找
# find      (不存在 返回-1)
# index     (不存在 程序就报错)
# count     (返回字符串出现的次数)

#rfind()    (右侧开始查找) 功能不变
#rindex()   (右侧开始查找) 功能不变

name = "hello world and itcast and itheima and Python"
#       find()
print(name.find('and'))
print(name.find('and',15,30))
print(name.find('ands',15,30))
print('---------------------------')
#        index()
# print(name.index('and'))
# print(name.index('and',15,30))
# print(name.index('ands',15,30))
print('-----------------------------')
#       count
print(name.count('and'))        # 3
print(name.count('and',15,30))  # 1
print(name.count('ands',15,30)) # 0