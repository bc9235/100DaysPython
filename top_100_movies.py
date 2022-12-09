import requests
from bs4 import BeautifulSoup

# Get site contents
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

# Input site contents and specify parser
soup = BeautifulSoup(contents, "html.parser")

# Get all movie title text
titles = soup.find_all(name="h3", class_="title")
title_text = [title.getText() for title in titles]
# Reverse the list so #1 at index 0
title_text = title_text[::-1]

# Write the titles to text file (utf-8 to get around UnicodeError)
with open("moviestowatch.txt", "w", encoding="utf-8") as file:
    for title in title_text:
        file.write(f"{title}\n")
