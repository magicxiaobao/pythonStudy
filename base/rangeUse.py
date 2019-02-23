# range()的使用 生成数列/数组
a = range(5)
print(a)  # range对象
print(list(a))  # 转换成数组
for i in a:
    print(i)

for i in range(1, 6):
    print(i)

# 奇数数组
nums = list(range(1, 13, 2))
print(nums)
# 偶数数组
nums = list(range(2, 14, 2))
print(nums)
