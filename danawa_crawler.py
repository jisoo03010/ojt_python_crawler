from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm # 얼마나 걸리는지 알려주는 툴
import time
import openpyxl
driver = webdriver.Chrome('C:/chromedriver.exe')

def main():
    wb = openpyxl.Workbook()
    ws = wb.active #현재 활성화된 셀을 보는것

    driver.get("https://www.danawa.com/")
    searchTag = driver.find_element(By.ID, "AKCSearch")
    searchTag.send_keys("RTX 3080") # input에다가 값을 넘겨줌
    # GPU, RAM 만 검색 가능
    searchTag.send_keys(Keys.ENTER)
    pageNo = 1 # 페이지처리
    idx = 1
    ws.append(['id', '상품명', '가격', '구매처 URL'])
    for i in range(pageNo, 2):
        print("PageNo : " + str(i))
        driver.execute_script("getPage(" + str(i) + ")")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "prod_item")
        for item in tqdm(itemList):
            if item.get_attribute("id") != "":
                title = item.find_element(By.CLASS_NAME, "prod_name")
                priceitem = item.find_elements(By.CLASS_NAME, "top5_item")
                #href = title.find_element(By.TAG_NAME,"a").get_attribute("href")
                #print(title.text)
                # for price in priceitem:
                #    print(title.text, " : ", price.text)

                #case 1
                # A태그를 통한 이동
                title.find_element(By.TAG_NAME, "a").click()
                #생성되 ㄴ파일에 앞으로 이동한다
                driver.switch_to.window(driver.window_handles[-1])
                title = driver.find_element(By.CLASS_NAME, "prod_tit")
                price = driver.find_element(By.CLASS_NAME, "lwst_prc")
                spec_list = driver.find_element(By.CLASS_NAME, "spec_list").text
                link = price.find_element(By.TAG_NAME, "a").get_attribute("href")
                print(title.text, price.text)
                ws.append([idx, title.text, price.text, link, spec_list])
                idx += 1
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(3)
        wb.save('danawa.xlsx')
if __name__ == '__main__':
    main()