"""
1、自定义列表的排列函数
2、自学字符串，列表，字典常用函数
3、英文单词反转
    how are you-->you are how
4、预习面向对象
"""


def arrange_list(list):
    for m in range(len(list) - 1):
        for n in range(m + 1, len(list)):
            if list[m] > list[n]:
                list[n], list[m] = list[m], list[n]


list01 = [1, 2, 5, 3, 4, 6, 7]
arrange_list(list01)
print(list01)


def reverse(str_list, start, end):
    """
    反转函数
    :param str_list:所需反转的列表
    :param start:开始
    :param end:结束
    """
    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1


def sentence_recerse(sentence):
    """

    :param sentence:
    :return:
    """
    str_list = list(sentence)
    i = 0
    long_list = len(str_list)
    while i < long_list:
        if str_list[i] != " ":
            start = i
            end = start + 1
            while (end < long_list) and (str_list[end] != " "):
                end += 1
            reverse(str_list, start, end - 1)
            i = end
        else:
            i += 1
    str_list.reverse()
    return (" ".join(str_list))


s = "where are you!"
s01 = sentence_recerse(s)
print(s01)
print()

str01 = "how are you"
list_result = str01.split(" ")
list_result = list_result[::-1]
str_result = " ".join(list_result)
print(str_result)
