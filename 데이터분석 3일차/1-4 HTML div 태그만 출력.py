import bs4

webPage = open('/Users/thdtjdals__/Desktop/데이터분석 2일차 자료/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div 태그를 찾아 찾은 값만 출력
tag_div = bsObject.find('div')
print(tag_div)