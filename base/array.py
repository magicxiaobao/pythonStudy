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



