import numpy as np
import cv2
import os
import time

# url = str(input("请输入图片地址："))


url = r'I:\工作汇总\公示发布\2021年公示\9月份\0901'


class BatchRename():
    def __init__(self):
        self.path = url  # 需更改文件地址，结尾需要有一定要有/

    @staticmethod
    def get_time():
        """
         获取日期编号
        Returns日期编号年月日
        -------

        """
        serial_num = int(time.strftime("%Y%m%d", time.localtime()))
        return serial_num

    def rename(self):
        filelist = os.listdir(self.path)  # 获取路径
        i = 1  # 图片初始名字
        for item in filelist:  # 利用for循环将filelist值赋予item内，循环执行
            if item.endswith('.jpg'):  # 用if检测文件结尾是否为.jpg，来判断是否是图片
                print(item)
                src = os.path.join(os.path.abspath(self.path), item)  # 定义原文件地址
                dst = url + "\\" + str(BatchRename.get_time()) + str("%02d" % i) + '.jpg'  # 新文件保存地址
                # img = cv2.imread(src, -1)  # 读取需要裁剪的图片(x,y)x=图片地址，y=读取方式
                img = cv2.imdecode(np.fromfile(src, dtype=np.uint8),
                                   cv2.IMREAD_COLOR)  # 读取需要裁剪的图片(x,y)x=图片地址，y=读取方式（中文路径读取）
                # img = cv2.cvtColor(img ,cv2.COLOR_LAB2BGR)
                new_size = cv2.resize(img, (1500, 900))  # 图片裁剪大小，手动进行更改
                # cv2.imwrite(dst, new_size)  # 新图片的保存路径
                cv2.imencode('.jpg', new_size)[1].tofile(dst)  # 新图片的保存路径（中文路径保存）
                i += 1


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
