import requests
import bs4
from pprint import pprint

# Goal is to Get a Book With a 2-star rating

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []

for n in range(1, 51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

pprint(two_star_titles)
