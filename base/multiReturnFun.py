import math


def multi_return(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = multi_return(3, 5, 2, 45)
print(x, y)
tuplex = multi_return(2, 4, 1, 30)
print(tuplex)
