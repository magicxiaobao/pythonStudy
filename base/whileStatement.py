# while 循环
result = 0
i = 1
while i < 9:
    result += i
    print(i)
    i += 1
    if i > 5:
        break  # 跳出循环
print(result)

j = 1
while j < 10:
    if j % 2 == 0:
        j += 1
        continue  # 继续循环,不执行下面的语句
    print(j)
    j += 1

# 循环数组
array = ["aaa", "bb", "cc"]
while array:
    a = array.pop()
    print(a)
