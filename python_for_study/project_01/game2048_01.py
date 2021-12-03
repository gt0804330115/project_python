"""
    2048 核心算法
"""

# 练习1：定义函数，将零元素移动到末尾
# 2 0 2 0 --> 2 2 0 0
# 0 2 2 0 --> 2 2 0 0
list01 = [2, 2, 2, 0]


# 定义排列函数
def move_zero(list_target):
    """
    将列表中的“0”元素移至列表末尾
    :param list_target: 旧列表
    """
    # 涉及到删除元素，倒序删除
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


# 定义合并函数
def merge_number(list_merge):
    move_zero(list_merge)
    for i in range(len(list_merge) - 1):
        # 相邻且相同
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            list_merge[i + 1] = 0
    move_zero(list_merge)


# 将二维列表，以表格的格式显示在控制台中
list01 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2],
]


def get_table(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()


# 定义向左移动函数
"""
    [2, 0, 0, 2]      [4, 0, 0, 0]
    [2, 2, 0, 0]      [4, 0, 0, 0]
    [2, 0, 4, 4]      [2, 8, 0, 0]
    [4, 0, 0, 2]      [4, 2, 0, 0]
"""


def move_left(map):
    for r in range(len(map)):
        # 从左往右获取行
        merge_number(map[r])


# 定义向右移动函数

def move_right(map):
    for r in range(len(map)):
        # 从右往左获取行
        list_merge = map[r][::-1]
        merge_number(list_merge)
        map[r][::-1] = list_merge


# 定义向上移动函数
def move_up(map):
    for c in range(4):
        list_merge = []
        # 从上往下获取列  形成一维列表
        for r in range(4):
            list_merge.append(map[r][c])
        # 交给 合并方法
        merge_number(list_merge)
        # 将合并后的结果list_merge ，还原给原二维列表
        for r in range(4):
            map[r][c] = list_merge[r]


# 定义向下移动函数

def move_down(map):
    for c in range(4):
        list_merge = []
        # 从下往上获取列  形成一维列表（从左到右）
        for r in range(3, -1, -1):  # 3  2  1  0
            list_merge.append(map[r][c])
        # 交给 合并方法
        merge_number(list_merge)
        # 将合并后的结果list_merge（从左到右） ，还原给原二维列表
        for r in range(3, -1, -1):
            map[r][c] = list_merge[3 - r]
