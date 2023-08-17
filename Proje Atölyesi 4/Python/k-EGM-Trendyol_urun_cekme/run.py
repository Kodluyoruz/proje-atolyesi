import requests
from bs4 import BeautifulSoup
import xlsxwriter

kok="https://www.trendyol.com"

workbook = xlsxwriter.Workbook("urunler.xlsx")
worksheet = workbook.add_worksheet("urunler")
worksheet.write(0,0,"Ürün Adı")
worksheet.write(0,1,"Fiyat")
worksheet.write(0,2,"Açıklama")
worksheet.write(0,3,"Görsel")
rows=0



def verileri_cek(url,rows):
    print("////////////////////////////////////////")
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    urun_adi=soup.find("h1",{"class":"pr-new-br"}).text
    print(urun_adi)
    fiyat=soup.find("span",{"class":"prc-dsc"}).text
    print(fiyat)
    aciklama=soup.find("ul",{"class":"detail-attr-container"}).text
    print(aciklama)
    foto=soup.find("div",{"class":"product-image-container"}).find_all("img")
    fotolar=[]
    for i in foto:
        print(i.get("src"))
        fotolar.append(i.get("src"))

    worksheet.write(rows,0,urun_adi)
    worksheet.write(rows,1,fiyat)
    worksheet.write(rows,2,aciklama)
    worksheet.write(rows,3,str(fotolar))
    


def urunlinklerial(kok):
    response=requests.get("https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&os=1&pi=4")
    soup=BeautifulSoup(response.content,"html.parser")
    veriler=soup.find("div",{"class":"prdct-cntnr-wrppr"}).find_all("a")
    urun_linkleri=[]
    rows=0
    for i in veriler:
        rows=rows+1
        url=kok+i.get("href")
        urun_linkleri.append(url)
        #print(url)
        verileri_cek(url,rows)

urunlinklerial(kok)
workbook.close()