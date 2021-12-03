# 5、扩展练习（定义函数，返回指定范围内的素数）
# 例如： 1--100


num = []


# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         num.append(i)
# print(num)


def get_prime(frist, last):
    import math
    num = []
    # i = 2
    for i in range(frist, last):
        # j = 2
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                break
        else:
            num.append(i)
    return num


num01 = get_prime(13, 67)
print(num01)
