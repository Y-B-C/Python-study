a = 1
b = a
print(b)        #   1

print(id(a))    #   140710479045008
print(id(b))    #   140710479045008

a = 2

print(b)        #   1
print(id(a))    #   140710479045040
print(id(b))    #   140710479045008

print('--------------------------------')
#  列表           列表是可变类型
aa = [10,20]
bb = aa
print(id(aa))   #2060111073672
print(id(bb))   #2060111073672
aa.append(30)
print(bb)       #[10, 20, 30]
print(id(aa))   #2642990289288
print(id(bb))   #2642990289288