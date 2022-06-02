import requests
from bs4 import BeautifulSoup

def getSchoolFoodData(id):
    schoolUrl = "https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do"
    response = requests.get(schoolUrl,params={"mlsvId":id})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select(".ta_l")

    date = result[1].text.strip()
    menu = result[3].text.strip()
    kcal = result[4].text.strip()

    print(date,menu)

def getScheduleData(id):
    url = "https://sdh.sen.hs.kr/dggb/module/schdul/selectSchdulDetailPopup.do"
    response = requests.get(url,params={"schdulId":id})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select(".ta_l")
    print(result[1].text.strip())
    print(result[2].text.strip())
    print(result[3].text.strip())
    print(result[4].text.strip())
    print("----------------")


def getIdFromCalender(url):
    result = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    li = soup.find_all(attrs={"title": "클릭하면 내용을 보실 수 있습니다."})
    for i in li:
        id = i.attrs['onclick'].split("'")[1]
        result.append(id)
    return result
def main():
    calendarURL = "https://sdh.sen.hs.kr/78401/subMenu.do"
    schoolFoodURL = "https://sdh.sen.hs.kr/78400/subMenu.do"
    result = getIdFromCalender(schoolFoodURL)
    for i in result:

        getSchoolFoodData(i)

if __name__ == '__main__':
    main()