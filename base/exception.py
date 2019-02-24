# 异常处理

try:
    print(10 / 0)
except ZeroDivisionError as zex:
    print("除0错误")
# else:
    # print("正常处理")
finally:
    print("End")
