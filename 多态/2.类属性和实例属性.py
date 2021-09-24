# 1.定义类，定义类属性
class Dog(object):
    tooth = 10
# 2.创建对象
wangcai = Dog()
xiaohei = Dog()
# 3.访问类属性：类对象
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)



# 修改类属性       类.类属性 = 值
# Dog.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)



# 通过对象修改类属性      ( 不能通过对象修改属性 )
wangcai.tooth = 200
print(Dog.tooth)       # 10
print(wangcai.tooth)   # 200
print(xiaohei.tooth)   #10
