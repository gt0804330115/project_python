"""
    将一个文件夹备份到ZIP文件中
"""
import zipfile, os


# 1、弄清楚ZIP文件的名称
def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    # 创建新ZIP文件
    print(f'Creating{zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # 遍历目录树并添加到ZIP文件
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    print('Done.')


backupToZip('I:\\工作汇总\\2021年工作')  # backToZip()函数只接收一个参数，即folder，这个参数是一个字符串路径，指向需要备份的文件夹。

# backupToZip.close()
