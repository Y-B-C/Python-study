def print_line():
    print('-'*20)

def print_lines(num):
    i =0
    while i < num:
        print_line()
        i+=1

print_lines(5)
print('----------------------======-----------------------')

#三个数求和
def sum_num(a,b,c):
    return a+b+c
result = sum_num(1,2,3)
print(result)

#求平均值
def average_num(a,b,c):
    sumResult = sum_num(a,b,c)
    return sumResult / 3
averageReasult = average_num(1,2,3)
print(averageReasult)