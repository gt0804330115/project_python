#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project   ：project_python 
@File      ：merge_pdf.py
@Author    ：guotong
@Date      ：2021/10/26 16:02 
@Features  ： 合并PDF，每个PDF的第一页不需要合并
"""
import PyPDF2, os

pdffiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdffiles.append(filename)
pdffiles.sort(key=str.lower)  # 列表按字典顺序排序
pdfwriter = PyPDF2.PdfFileWriter()  # 新建PDF文档，用来保存合并后的文档
# 打开每一个PDF文档
for filename in pdffiles:
    pdffileobj = open(filename, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    # 添加每一页
    for pagenum in range(1, pdfreader.numPages):  #第一页不合并
        pageobj = pdfreader.getPage(pagenum)
        pdfwriter.addPage(pageobj)
# 保存结果
pdfoutput = open('allminutes.pdf', 'wb')
pdfwriter.write(pdfoutput)
pdfoutput.close()
print('已完成')
