# Script for re-sizing/shrinking photos

import PIL
from PIL import Image
import os
os.chdir('/home/benbrew/Documents/compbioweb.github.io/images')


for number in range(12)[1:]:
    img = Image.open(str(number) + '.jpg')
    img = img.resize((180, 205), PIL.Image.ANTIALIAS)
    img.save(str(number) + '_new.jpg')




