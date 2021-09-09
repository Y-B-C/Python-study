# str = '1qwer3t'
# for i in str:
#     print(i)
# else:
#     print('循环正常介绍执行的else的代码')

print('-------------------------')

# str = '1qwer3t'
# for i in str:
#     if i == 'e':
#         break
#     print(i)
# else:
#     print('循环正常介绍执行的else的代码')

print('---------------------------')

# str = '1qwer3t'
# for i in str:
#     if i == 'e':
#         continue
#     print(i)
# else:
#     print('循环正常介绍执行的else的代码')
i=1
j=1
while j<10:
    i=1
    while i<j:
        print(f'{i}*{j}={i*j}',end='\t')
        i+=1
    print()
    j+=1