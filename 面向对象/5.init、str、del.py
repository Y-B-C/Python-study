# # 1.定义类：带参数的init: 宽度和高度： 实例方法：调用实例属性
# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def print_info(self):
#         print(f'宽度{self.width},高度{self.height}')
#
# # 2.创建对象，创建多个对象且属性不同：调用实例方法
# haier1 = Washer(10,20)
# haier1.print_info()

print('-----------------------------------------')
# class Washer():
#     def __init__(self):
#         self.width = 300
#
#     def __str__(self):
#         return '这是海尔洗衣机的说明书'
# haier1 = Washer()
# print(haier1)
print('-----------------------------------------')

class Washer():
    def __init__(self):
        self.width = 300
    def __del__(self):
        print('对象已经删除')

haier1 = Washer()
