import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다.> ")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

    # 애플 제품 제외 
    if "Apple" in name:
        print(" <Apple 상품 제외합니다> ")
        continue 

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

    # 리뷰 100개 이상, 평점 4.5이상만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        print(" <평점 없는 상품 제외합니다.> ")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text() # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예: (26)
        rate_cnt = rate_cnt[1:-1] # 예: 26
    else:
        rate_cnt = "평점 수 없음"
        print(" <평점 수 없는 상품 제외합니다.> ")
        continue
    
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)