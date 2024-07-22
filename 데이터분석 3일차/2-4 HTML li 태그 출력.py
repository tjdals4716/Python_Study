import bs4

webPage = open('/Users/thdtjdals__/Desktop/데이터분석 2일차 자료/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_li_all= bsObject.findAll('li')

# 첫 번째 방법
for tag_li in tag_li_all :
    print(tag_li.text)
print()

# 두 번째 방법
for i in range(len(tag_li_all)) :
    print(tag_li_all[i].text)