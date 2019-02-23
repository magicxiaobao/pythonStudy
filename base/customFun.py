def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def let_pass(x):
    pass


print(my_abs(232))
let_pass('xx')

print(my_abs('xxx'))
