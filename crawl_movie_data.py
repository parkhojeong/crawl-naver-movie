import time

import requests
import bs4
import csv

URL = "https://movie.naver.com/movie/point/af/list.naver?&page=1"
site_text = requests.get(URL, {}).text

# get html
web_page = bs4.BeautifulSoup(site_text, "lxml")

# parse
title_elements = web_page.find_all("td", {"class": "title"})

START_PAGE = 2
END_PAGE = 3
movie_data = []
for page in range(START_PAGE, END_PAGE):
    site_text = requests.get("https://movie.naver.com/movie/point/af/list.naver?&page={}".format(page), {}).text
    web_page = bs4.BeautifulSoup(site_text, "lxml")
    title_elements = web_page.find_all("td", {"class": "title"})

    for title in title_elements:
        movie_name = title.find("a").contents
        movie_score = title.find("em").contents
        movie_sentense = title.find("a", {"class": "report"}).get("onclick").split("', '")[2]

        if(movie_sentense == ""):
            continue

        movie_data.append({"movie": movie_name[0],  "sentense": movie_sentense, "score": movie_score[0]})

    time.sleep(0.5)

with open( "samples.csv", "w", newline="" ,encoding = 'utf8' ) as f:
    write = csv.writer(f)
    write.writerow(movie_data)
