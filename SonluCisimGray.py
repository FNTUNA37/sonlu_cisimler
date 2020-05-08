from sympy import Symbol
from sympy import poly
from sympy.abc import x,y,z
from sympy import *
from PIL import Image
import random
import numpy as np

rand=[]
GRAY = []
Cisim=[0,x]

def renk_sifreleme(RGB, kullanici):
    randomIndex=0
    list = []
    x = xfield(kullanici)
    for i in range(0, len(RGB),2):
            kare = expand((x ** 2) * (xfield(rand[randomIndex])))
            birinci = expand((x) * (xfield(RGB[i])))
            sabitSayi = expand(xfield(RGB[i + 1]))
            t = kare + birinci + sabitSayi
            t = duzenle(t)
            list.append(sayifield(t))
            randomIndex += 1
    return list

def duzenle(n):
    maxIndex = 12
    sonuc = 0
    temp = n.as_coefficients_dict()
    sonuc += temp[1]
    if len(Cisim) < maxIndex:
        for deger in range(1, len(Cisim)):
            sonuc+=(temp[x**deger]%2)*Cisim[deger]
    else:
        for deger in range(1, maxIndex):
            sonuc+=(temp[x**deger]%2)*Cisim[deger]

    return modlama(sonuc)

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def sayifield(n):
    n=modlama(n)
    n=n.as_coefficients_dict()
    sayi=0
    for ust in range(0,8):
        if n[x**ust]==1:
            sayi+=2**ust
    return sayi

def xfield(n):
    bitList=bitfield(n)
    bitList.reverse()
    sayi=0
    for index in range(0,len(bitList)):
        if bitList[index]==1:
            sayi+=x**index
    return sayi

def olustur():
    for i in range(2, 256):
        if i==8:
            Cisim.append(x**4+x**3+x**2+1)
        elif i>8:
            Cisim.append(duzenle(expand(Cisim[i - 1] * x)))
        else:
            Cisim.append(x**i)

    print("UZAY: " + str(x ** 8 + x ** 4 + x ** 3 + x ** 2 + 1))
    for a in range(0, len(Cisim)):
        print(str(a) + " --> " + str(Cisim[a]))

def modlama(list):
    if list == 0 or list==1:
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

def resim_bolme(imageName):
    im = Image.open(imageName).convert('L')
    im.save('greyscale.png')
    width = im.size[0]
    height = im.size[1]
    pix = im.load()

    for a in range(0, height):
        for b in range(0, width):
            GRAY.append(pix[b,a])

    for i in range(0, len(GRAY), 2):
        rand.append(random.randrange(256))

    for v in range(1, 6):
        print(v)
        newGRAY = renk_sifreleme(RGB=GRAY, kullanici=v)
        newim = Image.new("L", (int(width / 2), int(height)))
        newim.putdata(data=newGRAY)
        newim.save(str(v) + ".png")
        print(str(v)+" bitti")
    print("şifreleme işlemi bitti...")

olustur()
resim_bolme("test.jpg")