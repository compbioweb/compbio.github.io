# Script for re-sizing/shrinking photos

import PIL
from PIL import Image
import os
os.chdir('/home/benbrew/Desktop/pic')


for number in range(9)[1:]:
    img = Image.open(str(number) + '.jpg')
    img = img.resize((150, 190), PIL.Image.ANTIALIAS)
    img.save(str(number) + '_assoc.jpg')




