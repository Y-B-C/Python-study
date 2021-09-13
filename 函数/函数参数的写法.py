#位置参数


#   位 置 参 数
def user_info(name,age,gender):
    print(f'名字:{name},年龄：{age},性别:{gender}')

user_info('Tom',20,'男')
print('-------------------------------------------')

#   关 键 字 参 数
def user_info2(name,age,gender):
    print(f'名字:{name},年龄：{age},性别:{gender}')

user_info2('Tom',age=20,gender='男')
user_info2('python',gender='男',age=20)

print('-------------------------------------------')

#   缺 省 数 省
def user_info3(name,age,gender='男'):
    print(f'名字:{name},年龄：{age},性别:{gender}')

user_info3('Tom',age=20, )
user_info3('python',age=20,gender='女')

print('-------------------------------------------')

#    不 定 长 参 数     :返回的是元组
def user_info4(*args):
    print(args)
user_info4('TOM')
user_info4('TOM',18)
user_info4()
print('--------------------------------------------')

#收 集 所 有 关 键 参 数   :返回一个字典
def user_info5(**kwargs):
    print(kwargs)
user_info5()
user_info5(name='TOM')
user_info5(name='TOM',age=20)