import bs4

webPage = open('/Users/thdtjdals__/Desktop/데이터분석 2일차 자료/HTML/Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id':'myId1'})
print(tag)

tag = bsObject.find('div', {'class':'myClass1'})
print(tag)

tag = bsObject.findAll('div', {'class':'myClass1'})
print(tag)