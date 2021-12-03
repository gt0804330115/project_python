"""
    属性封装
"""


class Enemy:
    """
    敌人
    """

    def __init__(self, name, atk, speed, hp):
        self.name = name
        self.atk = atk
        self.speed = speed
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def speed(self):
        return self.__speed


    @speed.setter
    def speed(self, value):
        if 0 <= value <= 10:
            self.__speed = value
        else:
            self.__speed = 0
            print("攻击速度不在范围内，赋值失败")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            self.__hp = 0
            print("血量不在范围内，赋值失败")



# 练习：修改Enemy类，使用属性封装变量
class Wife:
    def __init__(self, name="", age=0):
        self.name = name  # 调用 @name.setter 修饰的方法
        self.age = age  # 调用 @age.setter 修饰的方法

    @property  # 拦截读取变量的操作
    def name(self):  # get_name()
        return self.__name

    @name.setter  # 拦截写入变量的操作
    def name(self, value):  # set_name()
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            self.__age = 0
            print("我不要")


w01 = Wife("铁锤", 86)
print(w01.name)
print(w01.age)

    


e01 = Enemy("xz", 100, 50, 200)
print(e01.name, e01.hp, e01.speed)
