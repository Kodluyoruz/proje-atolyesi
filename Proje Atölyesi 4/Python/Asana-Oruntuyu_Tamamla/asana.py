from random import randint
from PIL import Image, ImageDraw, ImageFont

"""
ilk sayiyi belirle
onceki sayının 2-6 katini al
onceki sayiya 10-30 arasini topla
bastan basla"""

def sabitleriBelirle():
    kat=randint(2,6)
    ilave=randint(10,30)
    return kat, ilave

def diziyiKur():
    while True:
        kat, ilave =sabitleriBelirle()
        algrt=f"A=X, B=X*{kat}, C=B+{ilave}..."
        ilkSayi=randint(2,12)
        counter=0
        dizi=[ilkSayi]
        currentNumber=ilkSayi
        while 3>counter:
            currentNumber=currentNumber*kat
            dizi.append(currentNumber)
            currentNumber=currentNumber+ilave
            dizi.append(currentNumber)
            counter+=1
        if dizi[-1]<1000:
            break
    return dizi, algrt

def soruyuKur():
    dizi, algrt=diziyiKur()
    index=randint(1,len(dizi)-1)
    cevap=dizi[index]
    dizi[index]="?"
    return dizi, cevap, algrt

def gorsel():
    zemin = Image.new('RGB', (800, 800), (200,200,200))
    yazici = ImageDraw.Draw(zemin)
    font =ImageFont.truetype("arial.ttf", 48, 0, encoding='tr-TR')
    yazici.text((10,10), "Aşana", fill="purple", font=font)
    dizi, cevap, algrt= soruyuKur()
    print(cevap, algrt)
    x=50
    for i in dizi:
        yazici.text((x,360),str(i),fill="blue", font=font)
        x+=100
    yazici.text((120,600),algrt,fill="black",font=font)
    yazici.text((360,700),str(cevap), fill="black",font=font)
    zemin.show()

gorsel()