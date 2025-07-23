import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) # <title>네이버 웹툰</title>
# print(soup.title.get_text()) # 네이버 웹툰
# print(soup.a) # soup 객체에서 처음 발견되는 a element를 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href의 속성 "값" 정보를 출력

# soup.find("a", attrs={"class":"AsideList__item--i30ly"}) # class = "AsideList__item--i30ly"인 a element를 찾아줘
# soup.find(attrs={"class":"AsideList__item--i30ly"}) # class = "AsideList__item--i30ly"인 어떤 element를 찾아줘

# print(soup.find("li", attrs={"class":"ContentTitle__title--e3qXt"}))
# rank1 = soup.find("li", attrs={"class":"ContentTitle__title--e3qXt"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank1.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))