from __future__ import absolute_import, unicode_literals
from celery import Celery
import requests
from bs4 import BeautifulSoup as bs
from .models import Post

# code to activate workers: celery -A info worker -l info --pool=solo --concurrency=10 -n worker1.%h

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def search_data_task(search_item):
    data = 0
    while data == 0:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
            url = 'https://www.amazon.com.br/s?k=' + str(search_item)
            resp = requests.get(url, headers=headers).text
            soup = bs(resp, 'html.parser')
            # print(soup)

            product_items = soup.find_all(class_='a-section a-spacing-medium')
            for product_item in product_items:

                try:
                    link = product_item.find('span')
                    link = link.find('a')['href']
                    link = 'https://www.amazon.com.br/' + link
                except:
                    link = "n/a"

                try:
                    image = product_item.find(class_="s-image")
                    image = image['src']
                except:
                    image = "n/a"

                try:
                    product = product_item.find(class_="a-size-base-plus a-color-base a-text-normal")
                    product = product.text
                except:
                    product = 'n/a'

                try:
                    price = product_item.find(class_="a-offscreen")
                    price = price.text
                except:
                    price = 'n/a'

                data = {
                    'search_term': search_item,
                    'product': product,
                    'price': price,
                    'image': image,
                    'link': link
                }
                post = Post(**data)
                post.save()
                print('data results', data)
        except:
            pass
        print('data')