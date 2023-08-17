
---

# Trendyol Ürün Bilgisi Çekme Uygulaması

Bu uygulama, Trendyol web sitesindeki ürünlerin bilgilerini çekmeyi amaçlayan bir Python betiğini içerir. Web scraping için `requests` ve `BeautifulSoup` kütüphaneleri kullanılmıştır. Toplanan veriler, bir Excel dosyasına kaydedilir.

## Gereksinimler

Uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `requests`: HTTP istekleri göndermek için kullanılır.
- `BeautifulSoup`: HTML içeriğini ayrıştırmak ve veri çekmek için kullanılır.
- `xlsxwriter`: Excel dosyası oluşturmak ve verileri kaydetmek için kullanılır.

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```
pip install requests
pip install beautifulsoup4
pip install XlsxWriter
```

## Nasıl Kullanılır

1. Kodu indirin veya kopyalayın.
2. Gerekli kütüphaneleri yükleyin.
3. Kodun başındaki `kok` değişkenine Trendyol web sitesinin ana sayfa URL'sini atayın.
4. Kodu çalıştırarak ürün bilgilerini toplayabilirsiniz.

```python
python run.py
```

Ürün bilgileri toplandıktan sonra, `urunler.xlsx` adında bir Excel dosyası oluşturulur. Bu dosyada her ürün için ad, fiyat, açıklama ve görsellerin bağlantıları bulunur.


---