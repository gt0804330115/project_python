"""
    转换日期格式
    MM-DD-YYYY  -->  DD-MM-YYYY
"""
import shutil, os, re

# 用正则表达式识别该模式


datePattern = re.compile(r'''
        (^.*?)          # all text before the date
        ([0-1]?\d)-     # one or two digits for the month
        ([0-3]?\d)-     # one or two digits for the day
        ((19|20)\d\d)   # four digits for the year
        (.*$)           # all text after the date
        ''', re.VERBOSE)

# TODO: Loop over the files in the working directory.

# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.

# 识别文件名中的日期部分
# 省略已完成的代码

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(6)

    # 省略已完成的代码
    euroFilename = (beforePart + dayPart + '-' + monthPart + '-' + yearPart +
                    afterPart)
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming {} to {}'.format(amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)  # uncomment after testing
