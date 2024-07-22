import bs4
import urllib.request

nateUrl = "https://www.naver.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'class':'snbArea'})

print('## 네이버의 메뉴 목록 ##')
li_list = tag.findAll('li')

# 메뉴 목록을 반복해서 출력
for li in li_list :
    print(li.text, end='  ' )