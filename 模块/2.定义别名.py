# 模块起别名
# import 模块名 as 别名

# 功能定义别名
# from 模块名 import 功能 as 别名


# 运行后暂停2秒打印hello
import time as tt
tt.sleep(2)
print('hello')

from time import sleep as s1
s1(2)
print('hello')