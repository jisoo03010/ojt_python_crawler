import requests
from bs4 import BeautifulSoup
# url = 'https://sdh.sen.hs.kr/78400/subMenu.do'
url = 'https://sdh.sen.hs.kr/78401/subMenu.do'

def ScheduleData(id):
    schoolURL = 'https://sdh.sen.hs.kr/dggb/module/schdul/selectSchdulDetailPopup.do'
    print(id)
    response = requests.get(schoolURL, params={'schdulId':id})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select('.ta_l')
    print(result[0].text.strip())
    print(result[1].text.strip())
    print(result[2].text.strip())
    print(result[3].text.strip())
    print(result[4].text.strip())
    print(result[5].text.strip())
    print('--------------')

def getSchoolFoodData(id):
    schoolURL = 'https://sdh.sen.hs.kr/dggb/module/mlsv/selectMlsvDetailPopup.do'
    response = requests.get(schoolURL, params={'mlsvId':id})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    result = soup.select('.ta_l')
    date = result[1].text.strip()
    menu = result[3].text.strip()
    kcal = result[4].text.strip()
    print(date)
    print(menu)
    print(kcal)
    print('------------------')

def main():
    result = getIdFromCalender(url)
    for i in result:
        ScheduleData(i)

def getIdFromCalender(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    result = []
    li = soup.find_all(attrs={'title': '클릭하면 내용을 보실 수 있습니다.'})
    for i in li:
        id = i.attrs['onclick'].split("'")[1]
        result.append(id)
    return result

if __name__ == "__main__":
    main()