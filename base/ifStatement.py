# base
mylist = ["guoguo", "xiaobao", "suisui", "lanlan", "honghong"]
for name in mylist:
    if name == "xiaobao":
        print(name, "is king.")
for name in mylist:
    if name != "xiaobao":
        print(name, "is superStar.")
if "guoguo" in mylist:
    print("果果在")
if "dahaizhong" not in mylist:
    print("大海忠不在")

if "xiaobao" in mylist or "guoguo" in mylist:
    print("家里有淘气鬼")
if "xiaobao" in mylist and "honghong" in mylist:
    print("家里有男士")

# advanced
point = 5
if point > 30:
    print("> 30")
elif point >= 20:
    print(">=20&&<=30")
elif point >= 10:
    print(">=10&&<20")
else:
    print("<10")
