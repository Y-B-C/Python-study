# mkdir()    创建文件夹-----------
import os
# os.mkdir('aa')

# rmdir():删除文件夹--------------
# os.rmdir('aa')

# getcwd():获取当前目录------------
# print(os.getcwd())

# chdir(目录)：改变默认目录--------------

# os.mkdir('aa')
# 需求：在aa里面创建bb文件： 1.切换目录到aa 2.创建bb
# 1.切换目录到aa
# os.chdir('aa')
# 2.创建bb
# os.mkdir('bb')

# listdir(目录)   获取目录列表-------------
# print(os.listdir())

# rename(目标文件名，新文件名)
# os.rename('test2.txt','test.txt')