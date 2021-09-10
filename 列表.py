# 查找

# 查找数据的  函数

# 查找数据的位置：index()
# 数据在列表中出现的次数：count()
# 访问列表长度：len()

# 判断是否存在：in-->在  not in-->不在
name_list = ['li','lu','Tom']
print(name_list[0])
print(name_list[1])
print(name_list[2])
print('-----------------------')

print(name_list.index('li'))

print(name_list.count('li'))

print(len(name_list))
print('-----------------------')

print('li'in name_list)
print('lis'in name_list)
print('li'not in name_list)
print('lis'not in name_list)
# 例子
name = input('请输入邮箱名字：')
if name in name_list:
    print(f'您输入的名字是{name},此用户已经存在')
else:
    print(f'您输入的名字是{name},可以注册')