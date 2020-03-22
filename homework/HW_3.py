import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
get=requests.get("https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309",headers=headers)

soup=BeautifulSoup(get.text,"html.parser")
soup_title=soup.find_all("a",attrs={"class":"title ellipsis"})
title=[t.get_text().strip() for t in soup_title]

soup_artist=soup.find_all("a",attrs={"class":"artist ellipsis"})
artist=[a.get_text().strip() for a in soup_artist]

for i in range(len(title)):
    print("{}순위 노래 : {} / 가수 : {}".format(i+1,title[i],artist[i]))