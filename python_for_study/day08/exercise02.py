"""
    练习：
    创建学生类
    数据：姓名，性别，年龄，成绩
    行为：print_self()
    定义函数：
        在学生列表中，根据姓名查找学生对象。
        在学生列表中，根据性别查找所有学生对象
        查找年龄大于20，成绩大于60的所有学生对象
"""


class Student:
    """
        学生类
    """

    def __init__(self, name, sex, age, grade):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade

    def print_self(self):
        print(self.name, self.sex, self.age, self.grade)


student_list = [
    Student("zs", "男", 18, 90),
    Student("ww", "男", 22, 70),
    Student("ls", "女", 21, 86),
    Student("zl", "女", 17, 88)
]


def get_student_for_name(student_list, name):
    for item in student_list:
        if item.name == name:
            return item


def get_student_for_sex(student_list, sex):
    # 使用列表存储多个结果
    list01 = []
    for item in student_list:
        if item.sex == sex:
            list01.append(item)
    return list01


re = get_student_for_sex(student_list, "男")
for item in re:
    item.print_self()


# if re != None:
#     re.print_self()
# else:
#     print("没有人员")


def get_sutdent_for_age_and_grade(student_list):
    list01 = []
    for item in student_list:
        if item.age > 20 and item.grade > 60:
            list01.append(item)
    return list01


re = get_sutdent_for_age_and_grade(student_list)
for item in re:
    item.print_self()
