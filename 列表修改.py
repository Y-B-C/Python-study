# 修改指定下标的数据：
# 逆序 reverse
# 排序(默认升序) sort()     sort(revers = True)---->降序

name_list = ['li','lu','Tom']
name_list[0] = 'aaa'
print(name_list)

# 逆序 reverse
list = [1,4,2,3,5,6]
# list.reverse()
# print(list)

# 排序 sort()   默认升序
# list.sort()
# print(list)

# sort(revers = True)---->降序
list.sort(reverse=True)
print(list)
