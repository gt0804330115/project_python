# coding=utf-8
import arcpy
import xlrd
import xlwt
import os

# workspace = arcpy.GetParameterAsText(0)
# out = arcpy.GetParameterAsText(1)
workspace = "D:\gdb\01"
out = "D:\gdb\02\02.gdb"

evefeature = []  # 存储所有要素要素路径+要素名
feature_classes = []  # 存储所有要素名
walk = arcpy.da.Walk(workspace, datatype="Any", type="Any")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        evefeature.append(os.path.join(dirpath, filename))
        if filename not in feature_classes:
            feature_classes.append(filename)
            print filename

for featurename in feature_classes:
    ls1 = []  # 存储同名要素路径+要素名
    for evefeatures in evefeature:
        int1 = len(featurename)
        int1 = int1 - int1 - int1
        if evefeatures[int1:] == featurename:
            ls1.append(evefeatures)
    arcpy.Merge_management(ls1, out + "/%s" % featurename)
    get = featurename + "get"
    arcpy.AddMessage(get)
