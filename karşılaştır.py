from sympy import Symbol
from sympy import poly
from sympy.abc import x,y,z
from sympy import *
from PIL import Image
import random
import numpy as np


bozukPixelSayisi=0
def load_image(name):
    return Image.open(name).convert('L')



im = load_image("lena.png")
im2 = load_image("birlesenResim.png")

width = im.size[0]
height = im.size[1]

pix = im.load()
pix2 = im2.load()

resim1=[]
resim2=[]


for a in range(0, height):
    for b in range(0, width):
        resim1.append(pix[b,a])

for c in range(0, height):
    for d in range(0, width):
        resim2.append(pix2[d, c])

for i in range(0,len(resim1)):

     if resim1[i]!=resim2[i]:
         print(i,resim1[i],resim2[i])
         bozukPixelSayisi+=1


print("bozuk pixel sayısı: ",bozukPixelSayisi)

