"""
    面向对象

"""


class Student():
    """
        学生
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def studying(self):
        print(self.name + "学习")

    def working(self):
        print(self.name + "工作")


student01 = Student("悟空", 28)
student01.studying()
student02 = Student("八戒", 29)
student02.working()
