import bs4

# utf-8을 사용해서 한글이 안깨지고 출력되도록 함
webPage = open('/Users/thdtjdals__/Desktop/데이터분석 2일차 자료/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)