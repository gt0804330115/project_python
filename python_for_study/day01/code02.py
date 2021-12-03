"""
    函数——返回值（结果）
"""


# 定义两个整数相加的函数
def add(number01, number02):
    result = number01 + number02
    # return:1、返回结果 2、退出方法
    return result


# 练习：定义检查列表是否具有相同元素的方法
def judge(list01):
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r] == list01[c]:
                return True
    return False


reslut = judge([1, 2, 3, 4, 5, 4, 3, 5, 6])
print(reslut)


def judge_quarter(month):
    if month < 1 or month > 12:
        return "输入有误"
    if month <= 3:
        return "春天"
    if month <= 6:
        return "夏天"
    if month <= 9:
        return "秋天"
    return "冬天"


judge_quarter(2)
