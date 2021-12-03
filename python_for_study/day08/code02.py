"""
    00 01 02 03
    10 11 12 13
    20 21 22 23
    需求：在某个元素基础上，获取每个方向，指定数量的元素。
               10             向右         3   -->  11 12 13
               21             向上         2   -->  11 01
               .........

"""


class Vector2:
    """
        向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

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


class DoubleListHElper:
    """
        二位列表助手类
    """

    # 在某个元素基础上，获取每个方向，指定数量的元素。
    @staticmethod
    def get_elements(list_target, v_pos, v_dir, count):
        result = []
        for i in range(count):
            # 位置   +=   方向
            # 10          01      -->11
            # 11          01      -->12
            # 12          01      -->13
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# 10                           向右            3   -->  11 12 13
re01 = DoubleListHElper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
print(re01)
# 21                           向上            2   -->  11 01
re02 = DoubleListHElper.get_elements(list01, Vector2(2, 1), Vector2.up(), 2)
print(re02)

re03 = DoubleListHElper.get_elements(list01, Vector2(2, 3), Vector2.left(), 3)
print(re03)

re04 = DoubleListHElper.get_elements(list01, Vector2(0, 2), Vector2.down(), 2)
print(re04)

re05 = DoubleListHElper.get_elements(list01, Vector2(2, 0), Vector2.right_up(), 2)
print(re05)
