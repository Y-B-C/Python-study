#函数要先定义再调用

# 确定选择功能界面：显示余额 存款 取款  # 封装函数
num = 22
def sel_func():
    print('显示余额')
    print('存款')
    print('取款')

#搭建整体框架
"""
输入密码登录后显示功能：    查询余额后显示功能   取完钱后显示功能
"""
print('登陆成功')
sel_func()

print('余额是100000')
sel_func()

print('取了10000元')
sel_func()