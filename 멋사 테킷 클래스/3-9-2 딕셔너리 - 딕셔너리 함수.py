# 7-11 딕셔너리 - 딕셔너리 함수

student = {
    "student_no" : "20231234",
    "major" : "English",
    "grade" : 1
}

# 데이터에 접근할때 사용하는 함수 : get (캡스톤때 했던 CRUD의 조회같음)
print(student.get("gpa", "해당 키-값 쌍이 없습니다"))

# 딕셔너리의 키를 반환하는 함수 : keys
# list로 감싸면 형변환이 됨(앞에 dict_keys 이게 없어짐)
print(list(student.keys()))

# 딕셔너리의 값을 반환하는 함수 : values
# list로 감싸면 형변환이 됨(앞에 dict_values 이게 없어짐)
print(list(student.values()))