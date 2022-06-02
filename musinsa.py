import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/chromedriver.exe')

def main():

    driver.get("https://www.musinsa.com/ranking/best")
    for i in range(5):
        type = driver.find_elements(By.XPATH, '//*[@id="goodsRankForm"]/div[1]/div[2]/dl/dd/ul/li')
        print(type[i].text)
        type[i].find_element(By.TAG_NAME, "a").send_keys(Keys.ENTER)
        time.sleep(1)

if __name__ == '__main__':
    main()