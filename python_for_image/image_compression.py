import os
from PIL import Image
import time

url = r'I:\工作汇总\公示发布\2021年公示\8月份\0825'


def get_time():
    """
     获取日期编号
    Returns日期编号年月日
    -------

    """
    serial_num = int(time.strftime("%Y%m%d", time.localtime()))
    return serial_num


# 源目录
project_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(project_dir, url)

# 输出目录
output = os.path.join(project_dir, url)


def modify():
    # 切换目录
    os.chdir(input)
    i = 1
    # 遍历目录下所有的文件
    for image_name in os.listdir(os.getcwd()):
        print(image_name)
        im = Image.open(os.path.join(input, image_name))
        im.thumbnail((1000, 800))
        new_name = str(get_time()) + str("%02d" % i) + '.jpg'
        im.save(os.path.join(output, new_name))
        i += 1


if __name__ == '__main__':
    modify()
