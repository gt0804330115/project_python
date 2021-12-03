"""
    对象计数器
"""


class Wife:
    """
        对象计数器
    """
    count = 0

    @classmethod
    def get_wife_count(cls):
        return cls.count

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Wife.count += 1

    def print_self(self):
        print(self.name, self.age)


w01 = Wife("ll", 20)
w02 = Wife("ss", 29)
print(Wife.get_wife_count())
