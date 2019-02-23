age = input("请输入你的年龄: ")
print("age=", age)
if age.isnumeric():
    if int(age) >= 30:
        print("现代年轻人")
    else:
        print("加油，年轻人")
else:
    print("火星年龄")
