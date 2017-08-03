'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone6 分辨率的大小。
'''

from PIL import Image
import os


path='pics'
result='result'

if not os.path.isdir(result):
    os.mkdir(result)

for pic_name in os.listdir(path):
    