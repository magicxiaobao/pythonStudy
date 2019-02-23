# 定义函数
def hello1():
    print("hello function")


hello1()


def hello2(name):
    print("hello", name)


hello2("xiaobao")
hello2(23)


def add(x, y):
    print(x + y)


add(10, 5)


# 参数默认值
def hello3(name="guoguo"):
    print("hi", name)


hello3()
hello3("suisui")


# 返回值
def add(x, y):
    return x + y


print(add(2, 9))


def makeurl(ip, port):
    str = ""
    str += "http://" + ip + ":"
    str += port
    return str


print(makeurl("192.168.3.1", "8080"))


def makedic(ip, port):
    return {
        "ip": ip,
        "port": port
    }


url = makedic("192.168.3.3", "8888")
print(url)
print(url["ip"])
print(url["port"])


# 可变参数
def add(*num):
    result = 0
    for n in num:
        result += n
    return result


print(add(1, 2, 3, 4, 5))


# 传递关键字参数,相当于传字典
def sendmail(**data):
    for key, val in data.items():
        print(key, "=", val)


sendmail(
    subject="PythonStudy",
    user="xiaobao",
    to="xiaobao1127@hotmail.com",
    tryTimes=5
)
