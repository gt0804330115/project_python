"""
    练习：
"""


class Enemy:
    """
        敌人
    """

    def __init__(self, name="", hp=0, atk=0.0, atk_speed=0.0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

    def print_self(self):
        print(self.name, self.hp, self.atk, self.atk_speed)


list_enemy = []
for i in range(2):
    e = Enemy()
    e.name = input("姓名：")
    e.hp = int(input("血量："))
    e.atk = float(input("攻击力："))
    e.atk_speed = float(input("攻击速度："))
    list_enemy.append(e)

for item in list_enemy:
    item.print_self()


def find_enemy(list_enemy, name):
    for item in list_enemy:
        if item.name == name:
            return item


re = find_enemy(list_enemy, "ds")
if re !=None:
    re.print_self()
else:
    print("没有找到")
