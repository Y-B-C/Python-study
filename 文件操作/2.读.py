# #  read()
# f = open('test.txt','r')
# # read不写参数表示读取所有
# print(f.read())
#
# f.close()

# # readlines
# f = open('test.txt','r')
# con = f.readlines()
# print(con)
# f.close()

# readline    一次读一行内容，调用多个，就读多行
f = open('test.txt','r')
con = f.readline()
print(con)
con = f.readline()
print(con)
con = f.readline()
print(con)
f.close()