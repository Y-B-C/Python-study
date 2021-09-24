# 1.定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    #定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth
# 2.创建对象，调用类方法
wangcai =Dog()
result = wangcai.get_tooth()
print(result)

print('-------------------静态方法-----------------')

# 1.定义一个类，定义静态方法
class Dog(object):
    @staticmethod
    def info_pring():
        print('这是一个静态方法')
# 2.创建对象
wc = Dog()
# 3.调用静态方法：  类  和  对象
wc.info_pring()

Dog.info_pring()