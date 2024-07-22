# 11-4 파일 다루기와 예외 처리 - 파일 쓰기
# 강의 천천히 다시보고 해보기

f = open('literature\poem.txt', 'a', encoding='UTF-8')

f.write("\n새로운 글이 작성되었습니다.")

f.close()