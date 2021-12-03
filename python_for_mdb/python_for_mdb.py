# 取出指定文件夹中所有MDB文件，读取其指定的FeatureClass，并将非空的GlobalID和SymbolRef记录到与FeatureClass同名的文本文件中
import os
import arcgis as arcpy

professional_dlc = {"ly": 1, "ya": 2, "ye": 3, "ad": 4, "jd": 5, "ja": 6,
                    "jc": 7, "zx": 8, "wd": 9, "aj": 10, "gy": 11, "fp": 13,
                    "yc": 14, "yd": 15, "wa": 16, "gs": 17, "as": 19, "sa": 21,
                    "dl": 24, "ay": 25, "ph": 26, "sb": 27, "sc": 28, "gj": 29,
                    "bd": 30, "lx": 34, "cl": 35, "jz": 36, "xf": 37, "yx": 38,
                    "ky": 39, "hc": 40, "kg": 41, "gt": 42, "gc": 44, "ys": 45,
                    "gh": 46, "gq": 47
                    }

target_folder = 'D:\T20161202'
file_names = (
    'BOUAN', 'BOULK', 'BOUNT', 'BOUPT', 'CTRLK', 'CTRPT', 'HYDAN', 'HYDLK', 'HYDNT', 'HYDPT', 'PIPAN', 'PIPLK', 'PIPNT',
    'PIPPT', 'RESAN', 'RESLK', 'RESNT', 'RESPT', 'ROAAN', 'ROALK', 'ROANT', 'ROAPT', 'TERAN', 'TERLK', 'TERNT', 'TERPT',
    'VEGAN', 'VEGLK', 'VEGNT', 'VEGPT')
source_folder = 'D:\T20161221_SymbolRef'
fields = ['GLOBALID', 'SymbolRef']
expression = u"GLOBALID IS NOT NULL"
for x in os.listdir(source_folder):
    file_path = source_folder + '\\' + x
    if os.path.isfile(file_path):
        print(file_path)
        mdb_paths = os.path.split(file_path)
        mdb_names = mdb_paths[1].split('.')
        if mdb_names[-1] == 'mdb':
            for file_name in file_names:
                feature_class = os.path.join(file_path, file_name)
                print(feature_class)
                result_path = target_folder + '\\' + file_name + '.txt'
                print(result_path)
                file_open = open(result_path, 'a')
                if arcpy.Exists(feature_class):
                    with arcpy.da.SearchCursor(feature_class, fields, where_clause=expression) as cursor:
                        for row in cursor:
                            if len(row[0]) > 0 and len(row[1]) > 0:
                                a_row = u'{0}+{1}'.format(row[0], row[1])
                                print(a_row)
                                file_open.write(a_row)
                                file_open.write('\n')
                file_open.close()
