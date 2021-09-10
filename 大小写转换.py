# 首字母大写：capitalize()
# 每个单词首字母大写:title()
# 所有字母转大写：upper()
# 所有字母转小写:lower()

# 删除左侧空白字符：lstrip()
# 删除右侧空白字符：rstrip()
# 删除两侧空白字符：strip()

# 字符串左对齐：ljust()
# 字符串右对齐：rjust()
# 居中对齐：center()
# 字符串.ljust(长度,填充字符)

# 判断是否以某个字符串开头：startswith()
# 判断是否以某个字符串结尾：endswith()


name = "hello world and itcast and itheima and Python"
str = name.capitalize()
print(str)

# 每个单词首字母大写:title()
str2 = name.title()
print(str2)

# 所有字母小写转大写：upper()
str3 = name.upper()
print(str3)

# 所有字母转小写:lower()
str4 = name.lower()
print(str4)

print('------------------删除空白字符----------------------')
# 删除左侧空白字符：lstrip()
str5 = name.lstrip()
print(str5)

# 删除右侧空白字符：rstrip()
str6 = name.rstrip()
print(str6)

# 删除两侧空白字符：strip()
str7 = name.strip()
print(str7)

print('----------------------------------------')
print(name.startswith('hello'))
print(name.endswith('Python'))
print(name.endswith('Pythons'))