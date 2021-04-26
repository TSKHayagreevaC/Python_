# from bs4 import BeautifulSoup
# import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.get("href"))
#     # print(tag.getText())
#     pass


# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.name)

# h3_heading = soup.find_all("h3", class_="heading")
# # print(h3_heading)

# company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select_one(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# # print(headings)


# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)


# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score").getText()]

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

# print(article_texts[largest_index])
# print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# Code On 100 greatest movies based on web rating given by watchers

import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
# for n in range(len(movie_titles) -1, 0, -1):
#     print(movie_titles[n])

movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

