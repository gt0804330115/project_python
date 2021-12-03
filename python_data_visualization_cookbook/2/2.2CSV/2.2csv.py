"""
    CSV文件处理
    1、打开ch02-data.csv文件
    2、首先读取文件头
    3、然后读取剩余行
    4、当发生错误时抛出异常
    5、读取完所有内容后，打印文件头和其余所有行
"""
import csv
import sys

filename = 'ch02-data.csv'
data = []
try:
    with open(filename) as f :
        reader = csv.reader(f)
        header = reader.__next__()
        data = [row for row in reader]
except csv.Error as e:
    print("Error reading CSV file at line %s: %s" %(reader.line_num,e))
    sys.exit(-1)
if header:
    print(header)
    print("=============")

for datarow in data:
    print(datarow)


