import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://www.labirint.ru/rating/?id_genre=-1&nrd=1"
r = requests.get(URL_TEMPLATE)

soup = bs(r.text, "html.parser")
books_names = [name.string for name in soup.find_all('span', class_='product-title')]
books_autors = []
books_prices = [price.span.string for price in soup.find_all('span', class_='price-val')]

for author in soup.find_all('div', class_='product-padding'):
    q = author.find('div', class_='product-author')
    if q:
        books_autors += [q.a['title']]
    else:
        books_autors += ['NO']

keys_list = ['book', 'author', 'price']

data = [{
    'book': books_names[i],
    'author': books_autors[i],
    'price': books_prices[i]
         } for i in range(len(books_names))]
#for name in books_names:
    #print(name.string)

#print(len(books_names), len(books_autors), len(books_prices))

print(data)
