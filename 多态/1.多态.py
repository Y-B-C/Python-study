#需求：警务人员和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作

# 1.定义父类，提供公共方法
class Dog(object):
    def work(self):
        pass
# 2.定义子类，子类重写父类方法
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')
class DruDog(Dog):
    def work(self):
        print('追查毒品......')
    # 定义人
class Person(object):
    def work_with_dog(self,dog):
        dog.work()
# 3.创建对象，调用不同的功能，传入不同的对象。
ad = ArmyDog()
dd = DruDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)