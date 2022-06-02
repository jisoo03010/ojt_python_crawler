from pprint import pprint

import requests
from bs4 import BeautifulSoup

# response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20220529")
# html = response.text
# soup = BeautifulSoup(html,"html.parser")
# elements = soup.select(".tit3")

# for element in elements:
#     print(element.text.strip())

response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220529")
html = response.text
soup = BeautifulSoup(html,"html.parser")
tr_elements = soup.select(".list_ranking > tbody > tr")

for element in tr_elements:
    if element.select_one(".tit5") is not None :
        title = element.select_one(".tit5")
        point = element.select_one(".point")
        print(title.text.strip(),point.text.strip())