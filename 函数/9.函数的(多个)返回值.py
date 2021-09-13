
#一个函数如果有多个return时，不能都执行，只执行第一个return
# def return_num():
#     return 1
#     return 2
# result = return_num()
# print(result)

def return_num():
    # return 1,2    返回的是元组
    # return后面可以直接书写  元组  列表  字典，返回多个值
    # return (12,13)
    # return [100,200]
    return {'name':'python','age':20}

result = return_num()
print(result)

