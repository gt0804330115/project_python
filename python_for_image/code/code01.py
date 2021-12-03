"""
    操作图像
"""
# 处理Image数据类型
# from PIL import Image
#
# catIm = Image.open('zophie.png')
# print(catIm.size)  # (816, 1088)
# width, height = catIm.size
# print(width)  # 816
# print(height)  # 1088
# print(catIm.filename)  # zophie.png
# print(catIm.format)  # PNG
# print(catIm.format_description)  # Portable network graphics  描述原始文件的图像格式
# catIm.save('zophie.jpg')

# from PIL import Image
#
# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purpleImage.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('transparenImage.png')

# 裁剪图像
# from PIL import Image
#
# catIm = Image.open('zophie.png')
# croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')

# 复制和粘贴图像到其他图像
# from PIL import Image
#
# catIm = Image.open('zophie.png')
# catCopyIm = catIm.copy()
# faceIm = catIm.crop((335, 345, 565, 560))
# print(faceIm.size)
# catCopyIm.paste(faceIm, (0, 0))
# catCopyIm.paste(faceIm, (400, 500))
# catCopyIm.save('pasted.png')
#
# catImWidth, catImHeight = catIm.size
# faceImWidath, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()
# for left in range(0, catImWidth, faceImWidath):
#     for top in range(0, catImHeight, faceImHeight):
#         print(left, top)
#         catCopyTwo.paste(faceIm, (left, top))
# catCopyTwo.save('tiled.png')

# 调整图像大小
from PIL import Image

catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize(int(width / 2), int(height / 2))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')
