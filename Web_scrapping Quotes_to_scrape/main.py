import requests
import bs4
from pprint import pprint

'''
TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
TASK: Get the names of all the authors on the first page.
TASK: Create a list of all the quotes on the first page.
TASK: Inspect the site and use Beautiful Soup to extract the top ten tags 
from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). 
HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top 
right tags, perhaps check the span.
TASK: Notice how there is more than one page, and subsequent pages look like this 
http://quotes.toscrape.com / page / 2 /.Use what you know about for loops and string concatenation 
to loop through all the pages and get all the unique authors on the website.Keep in mind there are many 
ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the 
last page with quotes.For debugging purposes, I will let you know that there are only 10 pages, so the last page is 
http://quotes.toscrape.com / page / 10 /, but try to create a loop that is robust enough that it 
wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!
'''

base_url = 'https://quotes.toscrape.com/'
result = requests.get(base_url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

for item in soup.select(".tag-item"):
    print(item.text)

page_url = base_url + 'page/' + str(9999999999999)
res = requests.get(page_url)
page_soup = bs4.BeautifulSoup(res.text, "lxml")

page_still_valid = True
authors = set()
page = 1

while page_still_valid:
    page_url = base_url + 'page/' + str(page)
    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        break
        # page_still_valid = False

    soup = bs4.BeautifulSoup(res.text, "lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

    page += 1

pprint(authors)
