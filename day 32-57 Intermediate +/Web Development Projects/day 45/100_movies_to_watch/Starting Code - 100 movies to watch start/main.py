import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
html_response= requests.get(URL)
# Write your code below this line 👇
soup= BeautifulSoup(html_response.text,"html.parser")

movie_titles=soup.find_all(name="h3", class_="title")
movie_list=[]

for movie in movie_titles:
    movie_list.append(movie.text)

movies = movie_list[::-1]

with open("top_100_movies.txt","w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
