class Washer():
    def wash(self):
        print('洗衣服')
    #获取对象属性
    def print_info(self):
        #self.属性名
        # print(self.width)
        print(f'洗衣机宽度是{self.width}')
        print(f'洗衣机高度是{self.height}')

haier1 = Washer()

haier1.width = 200
haier1.height = 800

#对象调用方法
haier1.print_info()