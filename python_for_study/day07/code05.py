"""
    形参传递方式
"""


def add_number(*args):
    result = 0
    for i in args:
        result += i
    return result


number01 = add_number(35, 2)
print(number01)


def fun05(*args, **kwargs):
    print(args)
    print(kwargs)


fun05(1, 2, 1, a=1, b=2)


def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun07(1, 2, 3, 4, 5, c=6, d=7, e=8, f=9)
