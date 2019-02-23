mylist = ["durant", "curry", "harden", "lebron"]
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[3].title())

# 修改元素
mylist[1] = "curry seth"
print(mylist)

# 增加元素
mylist.append("antetokounmpo")
print(mylist)

# 空数组增加元素
emptylist = []
emptylist.append("Python")
emptylist.append("Javascript")
emptylist.append("Ruby on Rails")
emptylist.append("Swift/Kotlin")
emptylist.append("Java")
print(emptylist)

# 删除元素
del emptylist[0]
print(emptylist)
print(emptylist[0])

# pop元素
deletedItem = emptylist.pop()
print(deletedItem)
print(emptylist)

# 指明删除
emptylist.remove("Ruby on Rails")
print(emptylist)

# 数组里可以存放不同类型的元素
mylist1 = ["hello", 22]
print(mylist1)
print(mylist1[0].title())

# 循环
family = ["suisui", "xiaobao", "guoguo"]
print("start.")
for name in family:
    print("\t", name)  # 缩进代码
print("end.")
print("start with index")
for i, name in enumerate(family):
    print("\t", i)
    print("\t", name)
print("end with index")

# 最大值，最小值，求和
nums = [1, 2, 3, 5]
print(min(nums))
print(max(nums))
print(sum(nums))

# lambda
nums = [val * 2 for val in range(1, 5)]
print(nums)

# 数组切片表示数组的一部分
country = ["china", "france", "japan", "america"]
print(country)
print(country[1])
# 切片
print(country[1:])
print(country[1:3])
print(country[:3])
# 循环切片
for c in country[1:3]:
    print(c)
# 复制切片
country1 = country[1:3]
print(country1)
country1.append("england")
print(country1)
print(country)

# 元祖 不可变的数组
# 通过小括号
meta = (1, 2, 3, 4,)
print(meta)
print(meta[0])
# 循环元祖
for i in meta:
    print(i)
# meta[0] = 5 元祖元素不可变
meta = ("a", "b", "c")
print(meta)
# meta[0] = "love" 元祖元素不可变
