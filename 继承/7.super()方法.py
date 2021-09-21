# 师父类   属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class School(object):
    def __int__(self):
        self.kongfu = '[学校煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    # super().__init__()
    # super().make_cake()
#2.定义徒弟类。继承师父类
class Prentice(Master,School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'


    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    #子类调用父类的同名属性和方法：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        #父类类名.函数（）
        #再次调用初始化的原因：这里想要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
    #需求：一次性调用父类School Master的方法
    def make_old_cake(self):
        #方法一：
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)

        #方法二：
        super().__init__()
        super().make_cake()
