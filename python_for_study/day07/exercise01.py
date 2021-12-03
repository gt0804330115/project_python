"""
    练习
"""

stems = 0


def fun01(a, b, c):
    a = 100
    b[0] = 200
    c = 300
    global stems
    stems += 1


num01 = 1
list01 = [2]
list02 = [3]
fun01(num01, list01, list02)
fun01(num01, list01, list02)
print(stems)
