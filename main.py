import requests
from bs4 import BeautifulSoup
response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220529")
html = response.text
soup = BeautifulSoup(html, "html.parser")
# print(soup)
# tr = soup.select("tr")
# elements = soup.select(".tit5")
# point = soup.select(".point")
# arr = []
#
#

# print(soup)
tr = soup.select(".list_ranking > tbody> tr")
print(tr)
for i in tr:
    if i.select_one(".tit5") is not None:
        point = i.select_one(".point")
        title = i.select_one(".tit5")
        print(title.text.strip(), point.text.strip())
