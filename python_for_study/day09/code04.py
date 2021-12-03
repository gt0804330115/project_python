"""
学生管理系统
"""


class StudentModel:
    """
        学生信息模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        Parameters
        ----------
        name  姓名，str类型
        age  年龄，int类型
        score  成绩，float类型
        id  编号（该学生对象的唯一标识）
        """

        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量，表示初始号码
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        Returns  存储学生对象的列表
        -------

        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        Parameters
        ----------
        stu_info  没有编号的学生信息

        -------

        """
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        """
            添加编号
        Returns  各学生唯一编号
        -------

        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id


"""测试添加学生功能
manager = StudentManagerController()
s01 = StudentModel("zs",24,100)
manager.add_student(s01)
manager.add_student(StudentModel("ls",24,100))
for item in manager.stu_list:
    print(item.name)
"""
