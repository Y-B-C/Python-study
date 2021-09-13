
# lambda 两个数字比大小，谁大返回谁
fn1 = lambda a,b: a if a>b else b
print(fn1(200,1300))

# 列表数据排序
students = [{'name':'TOM','age':20},
            {'name':'ROSE','age':16},
            {'name':'JACK','age':22}
            ]
# sort(key=lambda.....,reverse=bool数据)
# 1.name key对应的值进行升序排序
students.sort(key=lambda x:x['name'])
print(students)
# 2.name key对应的值进行降序排序
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
# 3.age key对应的值进行降序排序
students.sort(key=lambda x:x['age'])
print(students)
# 2.name key对应的值进行降序排序
students.sort(key=lambda x:x['age'],reverse=False)
print(students)
