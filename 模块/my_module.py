def testA(a,b):
    print(a*b)

# testA(1,2)
#只在但前文件中调用该函数，其他导入的文件内不符合该条件，则不执行该函数的调用
if __name__ == '__main__':
    testA(1,1)
