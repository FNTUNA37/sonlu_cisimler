from sympy import Symbol
from sympy import poly
from sympy.abc import x,y
from sympy import *
from PIL import Image
from datetime import datetime
import os

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

def eslenik(sayi):
    if sayi!=255:
        sonuc=255-sayi
    else:
        sonuc=sayi
    return sonuc

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

def kontrol(sayi):
    if sayi%255==0:
        return 255
    else:
        return sayi%255

def cozme(RGB,RGB2,RGB3,k1,k2,k3):
    list = []
    k1 = xfield(k1)
    k2 = xfield(k2)
    k3 = xfield(k3)
    k1 = cisim.index(k1)
    k2 = cisim.index(k2)
    k3 = cisim.index(k3)
    for i in range(0,len(RGB)):
        pixel = cisim.index(xfield(RGB[i]))
        pixel2 = cisim.index(xfield(RGB2[i]))
        pixel3 = cisim.index(xfield(RGB3[i]))

        if pixel == 0:
            birinciDenklem = 0 * y + 0
        else:
            birinciCarpan = kontrol((pixel+eslenik(cisim.index(modlama(expand((cisim[k1]+cisim[k2])*(cisim[k1]+cisim[k3])))))))
            birinciDenklem = kontrol(birinciCarpan+cisim.index(modlama(expand((cisim[k2]+cisim[k3])))))*y+kontrol(k2+k3+birinciCarpan)
        birinciDenklem=birinciDenklem.as_coefficients_dict()

        if pixel2 == 0:
            ikinciDenklem = 0 * y + 0
        else:
            ikinciCarpan = kontrol((pixel2 + eslenik(cisim.index(modlama(expand((cisim[k1] + cisim[k2]) * (cisim[k2] + cisim[k3])))))))
            ikinciDenklem = kontrol(ikinciCarpan + cisim.index(modlama(expand((cisim[k1] + cisim[k3]))))) * y + kontrol(k1 + k3 + ikinciCarpan)
        ikinciDenklem = ikinciDenklem.as_coefficients_dict()

        if pixel3 == 0:
            ucuncuDenklem = 0 * y + 0
        else:
            ucuncuCarpan = kontrol((pixel3 + eslenik(cisim.index(modlama(expand((cisim[k1] + cisim[k3]) * (cisim[k2] + cisim[k3])))))))
            ucuncuDenklem = kontrol(ucuncuCarpan + cisim.index(modlama(expand((cisim[k1] + cisim[k2]))))) * y + kontrol(k1 + k2 + ucuncuCarpan)
        ucuncuDenklem = ucuncuDenklem.as_coefficients_dict()

        # kare=(modlama((cisim[birinciDenklem[y ** 2]])+(cisim[ikinciDenklem[y**2]])+(cisim[ucuncuDenklem[y**2]])).subs(x,2))
        bir = (modlama((cisim[birinciDenklem[y]]) + (cisim[ikinciDenklem[y]]) + (cisim[ucuncuDenklem[y]])).subs(x,2))
        sabit = (modlama((cisim[birinciDenklem[1]]) + (cisim[ikinciDenklem[1]]) + (cisim[ucuncuDenklem[1]])).subs(x,2))
        list.append(bir)
        list.append(sabit)
    return list

def renkBirlestirme(height,width,newRED,newGREEN,newBLUE):
    newData=[]
    for i in range(0, (height*(width*2))):
        newData.append((newRED[i],newGREEN[i],newBLUE[i]))
    return newData

def birlestirme(k1,k2,k3):
    im = Image.open(str(k1) + '.png')
    im2 = Image.open(str(k2) + '.png')
    im3 = Image.open(str(k3) + '.png')

    width = im.size[0]
    height = im.size[1]

    pix = im.load()
    pix2 = im2.load()
    pix3 = im3.load()

    RED1 = []
    GREEN1 = []
    BLUE1 = []
    RED2 = []
    GREEN2 = []
    BLUE2 = []
    RED3 = []
    GREEN3 = []
    BLUE3 = []
    newData = []
    for a in range(0, height):
        for b in range(0, width):
            RGB = []
            RGB.append(pix[b, a])
            RGB.append(pix2[b, a])
            RGB.append(pix3[b, a])
            RED1.append(RGB[0][0])
            GREEN1.append(RGB[0][1])
            BLUE1.append(RGB[0][2])
            RED2.append(RGB[1][0])
            GREEN2.append(RGB[1][1])
            BLUE2.append(RGB[1][2])
            RED3.append(RGB[2][0])
            GREEN3.append(RGB[2][1])
            BLUE3.append(RGB[2][2])

    newRED = cozme(RGB=RED1, RGB2=RED2,RGB3=RED3,k1=k1,k2=k2,k3=k3)
    newGREEN = cozme(RGB=GREEN1, RGB2=GREEN2, RGB3=GREEN3,k1=k1,k2=k2,k3=k3)
    newBLUE = cozme(RGB=BLUE1, RGB2=BLUE2, RGB3=BLUE3,k1=k1,k2=k2,k3=k3)
    newData=renkBirlestirme(height,width,newRED,newGREEN,newBLUE)
    newim = Image.new("RGB", (int(width * 2), int(height)))
    newim.putdata(data=newData)
    newim.save("birlesenResim.png")

baslangic=datetime.now()
cisim=[0,x]
olustur()
birlestirme(2,3,5)
bitis=datetime.now()
print(bitis-baslangic)