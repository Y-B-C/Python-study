
# 方法一
"""
1.导入
    import 包名.模块名
2.调用功能
    包名.模块.功能
"""
# import python.mypackage.my_module1
# python.mypackage.my_module1.info_print1()


# 方法二     注意：设置__init__.py文件里面的all列表，添加的是允许导入的模块
#                否则无法使用

"""
import 包名 import *
模块名.目标
"""
from python.mypackage import *
my_module1.info_print1()


