from sympy import Symbol
from sympy import poly
from sympy.abc import x,y
from sympy import *
from PIL import Image
import random

def renk_sifreleme(RGB, kullanici):
    randomIndex = 0
    list = []
    y = xfield(kullanici)
    for i in range(0, len(RGB), 2):
        kare = expand((y ** 2) * (xfield(rand[randomIndex])))
        birinci = expand((y) * (xfield(RGB[i])))
        sabitSayi = expand(xfield(RGB[i + 1]))
        t = kare + birinci + sabitSayi
        t = duzenle(t)
        list.append(sayifield(t))
        randomIndex += 1
    return list

def newImage(height,width,newRED,newGREEN,newBLUE):
    newData=[]
    for i in range(0, int(height*(width/2))):
        newData.append((newRED[i],newGREEN[i],newBLUE[i]))
    return newData

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def xfield(n):
    bitList=bitfield(n)
    bitList.reverse()
    sayi=0
    for index in range(0,len(bitList)):
        if bitList[index]==1:
            sayi+=x**index
    return sayi

def sayifield(n):
    n=modlama(n)
    n=n.as_coefficients_dict()
    sayi=0
    for ust in range(0,8):
        if n[x**ust]==1:
            sayi+=2**ust
    return sayi

def olustur():
    for i in range(2, 256):
        if i==8:
            cisim.append(x**4+x**3+x**2+1)
        elif i>8:
            cisim.append(duzenle(expand(cisim[i - 1] * x)))
        else:
            cisim.append(x**i)

    print("UZAY: " + str(x ** 8 + x ** 4 + x ** 3 + x ** 2 + 1))
    for a in range(0, len(cisim)):
        print(str(a) + " --> " + str(cisim[a]))

def modlama(list):
    if list == 0:
        return list
    else:
        list = list.as_coefficients_dict()
        sonuc = 0
        for i in range(0, 15):
            if i == 0:
                sonuc += list[1] % 2
            else:
                sonuc += ((list[x ** i] % 2) * (x ** i))
        return sonuc

def duzenle(n):
    maxIndex = 12
    sonuc = 0
    temp = n.as_coefficients_dict()
    sonuc += temp[1]
    if len(cisim) < maxIndex:
        for deger in range(1, len(cisim)):
            sonuc+=(temp[x**deger]%2)*cisim[deger]
    else:
        for deger in range(1, maxIndex):
            sonuc+=(temp[x**deger]%2)*cisim[deger]

    return modlama(sonuc)

def resim_bolme(imageName):
    im = Image.open(imageName)

    width = im.size[0]
    height = im.size[1]
    pix = im.load()
    RED = []
    GREEN = []
    BLUE = []

    for a in range(0, height):
        for b in range(0, width):
            RGB = []
            RGB.append(pix[b, a])
            RED.append(RGB[0][0])
            GREEN.append(RGB[0][1])
            BLUE.append(RGB[0][2])

    for i in range(0, len(RED), 2):
        rand.append(random.randrange(256))

    for v in range(1, 6):
        print(str(v)+" RED")
        newRED = renk_sifreleme(RGB=RED, kullanici=v)
        print(str(v) + " GREEN")
        newGREEN = renk_sifreleme(RGB=GREEN, kullanici=v)
        print(str(v) + " BLUE")
        newBLUE = renk_sifreleme(RGB=BLUE, kullanici=v)
        newData = newImage(height, width, newRED, newGREEN, newBLUE)
        newim = Image.new("RGB", (int(width / 2), int(height)))
        newim.putdata(data=newData)
        newim.save(str(v) + ".png")
        print(str(v),"finish")

cisim=[0,x]
rand = []
olustur()
resim_bolme("lena.png")