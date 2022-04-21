import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
all_movies = soup.find_all(name='h3', class_='title')
movie_titles = [movie.getText() for movie in all_movies]
reversed_movie_titles = movie_titles[::-1]
pprint(reversed_movie_titles)

with open('movies.txt', 'w', encoding='UTF-8') as f:
    for movie in reversed_movie_titles:
        f.write(f'{movie}\n')

