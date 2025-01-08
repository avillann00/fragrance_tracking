from bs4 import BeautifulSoup
import requests

def all_websites():
    websites = ['venba', 'olfactory', 'nm', 'aura', 'ediscount', 'jetee']
    
    return websites

def venba_get_price(url):
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        price = soup.find('span', class_='product__price--sale')
        
        if price:
            price = price.get_text(strip=True)

            return price
         
    except requests.exceptions.RequestException as e:
        print(e)

def olfactory_get_price(url):
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        price = soup.find('span', class_='price-item price-item--sale price-item--last')
        
        if price:
            price = price.get_text(strip=True)

            return price
         
    except requests.exceptions.RequestException as e:
        print(e)
def nm_get_price(url):
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        price = soup.find('span', class_='Pricingstyles__RetailPrice-gnVaue hMfJba')
        
        if price:
            price = price.get_text(strip=True)

            return price
         
    except requests.exceptions.RequestException as e:
        print(e)

def aura_get_price(url):
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        price = soup.find('span', id='productPrice-product-template')
        
        if price:
            price = price.find('span', class_='visually-hidden')

            price = price.get_text(strip=True)

            return price
         
    except requests.exceptions.RequestException as e:
        print(e)

def ediscount_get_price(url):
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        price = soup.find('span', class_='price-value')
        
        if price:
            price = price.get_text(strip=True)

            return price
         
    except requests.exceptions.RequestException as e:
        print(e)

def jetee_get_price(url):
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        price = soup.find('span', id='ProductPrice-7551889309939', class_='product__price')

        if price:
            price = price.get_text(strip=True)

            return price
    except requests.exceptions.RequestException as e:
        print(e)

"""
def joma_get_price(url): # wip
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'lxml')

        a = soup.find('div', class_='price-wrapper with-coupon')
        if a:

            price_div = a.find('div', class_='now-price')

            if price_div:
                price_span = price_div.find('span')

                if price_span:
                    price = price_span.get_text(strip=True)

                    return price
         
    except requests.exceptions.RequestException as e:
        print(e)

def fragbuy_get_price(url): # wip
    try:
        response = requests.get(url)

        content = response.text
        soup = BeautifulSoup(content, 'lxml')

        c = soup.find('div', class_='container')

        if c:
            b = c.find('div', class_='row')

            if b:
                a = b.find('div', class_='col-lg-7 col-md-7 col-sm-6 col-xs-12 product_info')

                if a:
                    price_h4 = a.find('h4', class_='detail_price')

                    if price_h4:
                        price_sale = price_h4.find('span', class_='sale_price')

                        if price_sale:

                            price = price_sale.find('span', class_='money')

                            if price:
                                price = price.get_text(strip=True)

                                return price
         
    except requests.exceptions.RequestException as e:
        print(e)

"""
