# 1.自定义异常类   继承Exception
class ShortInputError(Exception):
    def __int__(self,length,min_len):
        self.length = length
        self.min_len = min_len
        #设置异常描述信息
    def __str__(self):
        return f'输入的密码长度是{self.length},密码不能少于{self.min_len}'
# 2.抛出异常   raise 异常类名()
def main():
    # 2.抛出异常：尝试执行：用户输入密码，如果长度小于3，抛出异常1
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            #抛出异常类创建的对象
            raise ShortInputError(len(password),3)

    # 3.捕获异常
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')
main()