from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

article_links = []
article_texts = []
article_upvotes = []

news = soup.find_all(class_="titleline")
for heading in news:
    article_links.append(heading.find(name="a").get("href"))
    article_texts.append(heading.find(name="a").getText())

scores = soup.find_all(class_="score")
for score in scores:
    article_upvotes.append(int(score.getText().split(" ")[0]))

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_links[largest_index])
