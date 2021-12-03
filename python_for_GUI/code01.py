"""
    用GUI自动化控制键盘和鼠标
"""
# 电脑分辨率
# import pyautogui
#
# wh = pyautogui.size()
# print(wh)  # Size(width=1920, height=1080)
# 移动鼠标指针
# import pyautogui
#
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

import pyautogui

# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)  # right
#     pyautogui.move(0, 100, duration=0.25)  # down
#     pyautogui.move(-100, 0, duration=0.25)  # left
#     pyautogui.move(0, -100, duration=0.25)  # up

# 获取鼠标指针位置
print(pyautogui.position())

# 画图
# import pyautogui, time
#
# time.sleep(5)  # 5秒延迟
# pyautogui.click()
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2)
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2)
#     pyautogui.drag(-distance, 0, duration=0.2)
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.2)

# 滚动鼠标
# pyautogui.scroll(200)

# 规划鼠标运动
# import pyautogui
# pyautogui.mouseInfo()

fw = pyautogui.getActiveWindow()
print(fw.title)
