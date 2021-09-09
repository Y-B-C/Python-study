# str = '1qwerrt'
# for i in str:
#     print(i)
print('--------------------------')

# str = '1qwerrt'
# for i in str:
#     if i == 'e':
#         print("当遇到e时，程序退出")
#         break
#     print(i)
print('---------------------------')

str = '1qwerrt'
for i in str:
    if i == 'e':
        print("当遇到e时，e不打印")
        continue
    print(i)