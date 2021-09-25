# 需求1:把code文件夹所有文件重命名 Python__xxx
import os
# 1.找到所有文件：获取code文件夹的目录列表 --listdir()
flag = 1
file_list = os.listdir('666')
print(file_list)

#2.构造名字
for i in file_list:
    if flag == 1:
        #new_name = 'Python_'+原文件i
        new_name = 'Python_'+i
    elif flag == 2:
        #  删除前缀
        num = len('Python_')

#3.重命名
    os.rename(i,new_name)