"""
    练习
"""


# 1、定义判断是否是奇数
# number = int(input("请输入整数："))
# if number % 2:
#     print("奇数")
# else:
#     print("偶数")


def judge_odd(number):
    # if number % 2 == 1:
    #     return True
    # else:
    #     return False
    # return True if number % 2 == 1 else False (条件表达式)
    return number % 2 == 1


# 2、定义根据月份返回天数的方法
# 要求： 考虑2月，如果是闰年返回29天，否则返回28天。
# month = int(input("请输入月份："))
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("28天")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print("30天")
# else:
#     print("31天")

# 向外返回的结果，类型应该统一
def is_leap_year(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)


def get_day(year, month):
    if month < 1 or month > 12 or year < 0:
        return 0
    if month == 2:
        # if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
        #     return 29
        # return 28
        return 29 if is_leap_year else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


# 3、定义获取最小值方法。
# min = list01[0]
# for i in range(1, len(list01)):
#     if min > list01[i]:
#         min = list01[i]
# print(min)

def get_min(list01):
    min = list01[0]
    for i in range(1, len(list01)):
        if min > list01[i]:
            min = list01[i]
    return min


# 4、定义函数，判断字符串中存在的中文字符的数量
# 中文编码范围： 0x4E00   ord(字符)    0x9FA5

def get_count(str01):
    count01 = 0
    for r in str01:
        if ord(r) >= 0x4E00 and ord(r) <= 0x9FA5:
            count01 += 1
    return count01


# 5、扩展练习（定义函数，返回指定范围内的素数）
# 例如： 1--100


# num = []
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
    """
    判断是否是素数
    :param frist:
    :param last:
    :return:
    """
    num = []
    # i = 2
    for i in range(frist, last + 1):
        # j = 2
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num.append(i)
    return num

# def get_prime(frist, last):
#     import math
#     num = []
#     for i in range(frist, last):
#         for j in range(2, int(math.sqrt(i))):
#             if i % j == 0:
#                 break
#         else:
#             num.append(i)
#     return num
