from sympy import Symbol
from sympy import poly
from sympy.abc import x,y
from sympy.core.sympify import kernS
from sympy import *
from PIL import Image
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
    if list==0:
        return 1
    else:
        list=list.as_coefficients_dict()
        sonuc=0
        for i in range(0,15):
            if i==0:
             sonuc+=list[1]%2
            else:
                sonuc+=((list[x**i]%2)*(x**i))
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

def eslenik(sayi):
    if sayi!=255:
        sonuc=255-sayi
    else:
        sonuc=sayi
    return sonuc

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
            birinciDenklem = 0*y+0
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

def birlestirme(k1,k2,k3):
    im = Image.open(str(k1) + '.png')
    im2 = Image.open(str(k2) + '.png')
    im3 = Image.open(str(k3) + '.png')

    width = im.size[0]
    height = im.size[1]

    pix = im.load()
    pix2 = im2.load()
    pix3 = im3.load()

    GRAY1 = []

    GRAY2 = []

    GRAY3 = []

    newData = []
    for a in range(0, height):
        for b in range(0, width):
            GRAY1.append(pix[b, a])

    for c in range(0, height):
        for d in range(0, width):
            GRAY2.append(pix2[d, c])

    for e in range(0, height):
        for f in range(0, width):
            GRAY3.append(pix3[f, e])

    newGRAY = cozme(RGB=GRAY1, RGB2=GRAY2,RGB3=GRAY3,k1=k1,k2=k2,k3=k3)
    newim = Image.new("L", (int(width * 2), int(height)))
    newim.putdata(data=newGRAY)
    newim.save("birlesenResim.png")

cisim=[0,x]
olustur()
birlestirme(1,3,5)
print('finish')