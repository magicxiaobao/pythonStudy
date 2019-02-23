#字符串其实是数组
str = "abcdefg"
print(str[0])
print(str[0:4])
print(str[2:])
print(str[:4])

#字符串拼凑
a1 = "s"
a2 = "os"
print(a1 + a2)
print(a1, a2)

#一些api
str1 = "hello World"
print(str1)
print(str1.title())
print(str1.upper())
print(str1.isupper())
print(str1.lower())
print(str1.islower())

#转义字符
str2 = "I can : \n\tJava\n\tJavaScript\n\tPython"
print(str2)

#删除空白
str3 = " You can You up "
print("|" + str3 + "|")
print("|" + str3.rstrip() + "|")
print("|" + str3.lstrip() + "|")
print("|" + str3.strip() + "|")