#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project   ：project_python 
@File      ：txt_to_excel.py
@Author    ：guotong
@Date      ：2021/11/2 9:14 
@Features  ： 
"""
import xlwt
import re

f = open('export1.txt')
x = 1
z = 0
xls = xlwt.Workbook()
sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
lines = []
# 正则表达式
# pattern01 =r'^[A-Za-z]+$'
# pattern02 = r'^\w+$'
pattern03 = r'[\u4e00-\u9fa5]|.es|No|(…\n)'

while True:
    line = f.readline()
    if not line:
        break
    # match01 = re.search(pattern01,line)
    # match02 = re.search(pattern02,line)
    match03 = re.search(pattern03, line)
    if match03 == None :
        lines.append(line)
print(lines)

for x in range(len(lines) - 1):
    if z < len(lines):
        sheet.write(x, 0, lines[z])
        z += 1
        sheet.write(x, 1, lines[z])
        z += 1
    else:
        break

xls.save('export.xls')
