from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url로 이동

time.sleep(3)

browser.find_element(By.CLASS_NAME, "FullscreenPopup_close").click()

time.sleep(3)

# 가는 날 클릭
browser.find_element(By.CLASS_NAME, "tabContent_option___mYJO.select_Date__Potbp").click()

# 이번 달 27일, 28일 선택
browser.find_elements(By.CLASS_NAME, "sc-cwHptR.hFwLsU.num")[26].click() # [26] -> 달력에서 27일선택
browser.find_elements(By.CLASS_NAME, "sc-cwHptR.hFwLsU.num")[27].click() # [27] -> 달력에서 28일선택

"""
# 제주도 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button").click()

# 항공권 검색
browser.find_element(By.LINK_TEXT, "항공권 검색").click()
"""

"""
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(By.XPATH, "//*[@id='__next']/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button"))
    # 성공했을 때 동작 수행
    print(elem.quit)# 첫번째 결과 출력
finally:
    browser.quit()
"""
    
# 첫번째 결과 출력
# elem = browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[8]/div[2]/div[2]/div[2]/ul[1]/li[1]/button")
# print(elem.text)


time.sleep(300)