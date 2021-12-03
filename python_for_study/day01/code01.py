# list01 = [1, 2, 3, 4, 52, 34, 56, 467, 65, 33, 2]
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] > list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01)

def rect(r_count, c_count):
    for r in range(r_count):
        for c in range(c_count):
            print("*", end="")
        print()


rect(5, 6)


def triangle(height,char):
    """
    打印三角形
    :param height:
    :param char:
    :return:
    """
    for r in range(height):
        for c in range(r + 1):
            print(char, end="")
        print()


triangle(6,"!")
