import requests
from bs4 import BeautifulSoup
from db_islemleri import db_islemleri


def fiyati_donustur(fiyat):
    donusturulmus_fiyat0 = fiyat.replace("TL", "")
    donusturulmus_fiyat05 = donusturulmus_fiyat0.replace(".", "")
    donusturulmus_fiyat1 = float(donusturulmus_fiyat05.replace(",", "."))
    return donusturulmus_fiyat1


def get_product(url,hedef):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")
    get_product.title = soup.find(id="productTitle").getText().strip()
    get_product.price = fiyati_donustur(
        soup.find("span", class_="a-offscreen").getText().strip())
    info = (get_product.title[:75] +
            '..') if len(get_product.title) > 75 else get_product.title
    db_islemleri.db_ekle(info, get_product.price, url,hedef)


def get_price_for_update(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")
    return fiyati_donustur(soup.find("span", class_="a-offscreen").getText().strip())
