class Washer():
    def wash(self):
        print('洗衣服')
        print(self)
haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()

#  对象名.属性名 = 值
haier1.width = 200
haier1.height = 800

print(f'洗衣机宽度是{haier1.width}')
print(f'洗衣机宽度是{haier1.height}')