# break--->终止此循环
# continue---->退出当前循环，继续执行下一次循环代码

i = 1
while i <=5:
    if i ==4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i +=1

print('---------------------------')

# j = 1
# while j <=5:
#     if i ==3:
#         print('有虫子，这个苹果不吃了')
#         continue
#     print(f'吃了第{i}苹果')
#     i+=1
#   死循环

j = 1
while j <=5:
    if j ==3:
        print('有虫子，这个苹果不吃了')
        j += 1
        continue
    print(f'吃了第{j}苹果')
    j+=1




