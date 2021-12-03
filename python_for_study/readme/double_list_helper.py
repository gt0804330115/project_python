"""
    二维列表工具
"""


class Vector2:
    """
        向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 将方法转移到类中，就是静态方法
    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)

    @staticmethod
    def right_up():
        return Vector2(-1, 1)

    @staticmethod
    def right_down():
        return Vector2(1, 1)

    @staticmethod
    def left_up():
        return Vector2(-1, -1)

    @staticmethod
    def left_down():
        return Vector2(1, -1)


class Double_list_helper:
    """
        二位列表助手类
            注释：在开发过程中，所有对二维列表的常用操作
    """

    @staticmethod
    def get_elements(list_target, v_poc, v_dir, count):
        result = []
        for i in range(count):
            v_poc.x += v_dir.x
            v_poc.y += v_dir.y
            result.append(list_target[v_poc.x][v_poc.y])
        return result


# 测试．．．．．．．．．．．．．
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# 10               向右　　　　　３　　　　－－> 11 12  13
re01 = Double_list_helper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
print(re01)

# 练习１：在二维列表中，获取23位置，向左，３个元素．
re02 = Double_list_helper.get_elements(list01, Vector2(2, 3), Vector2.left(), 3)
# 练习２：在二维列表中，获取02位置，向下，２个元素．
re02 = Double_list_helper.get_elements(list01, Vector2(0, 2), Vector2.down(), 2)
# 练习３：在二维列表中，获取20位置，右上，２个元素．
re02 = Double_list_helper.get_elements(list01, Vector2(2, 0), Vector2.right_up(), 2)
print(re02)