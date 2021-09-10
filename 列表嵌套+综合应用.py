name_list = [['li','lu','Tom'],['小民','张三','李四'],['liue','xiao','hong']]
print(name_list)

print(name_list[0])  # ['li', 'lu', 'Tom']

print(name_list[1][1])   # 张三
print('-----------------------------------------')
import random
# 需求：8位老师，3个办公室，将8位老师随机分配到3个办公室
# 打印办公室的人数和老师名字
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]

for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)
# print(offices)
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)} 老师分别是：')
    for name in office:
        print(name)
    i+=1