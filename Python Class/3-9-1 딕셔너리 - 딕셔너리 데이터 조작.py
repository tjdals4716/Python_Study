# 7-10 딕셔너리 - 딕셔너리 데이터 조작

student = {
    "student_no" : "20231234",
    "major" : "English",
    "grade" : 1
}

# 딕셔너리 추가 (원하는 값을 추가적으로 작성하면 됨)
student["gpa"] = 4.5
print(student)

# 딕셔너리 수정 (기존의 값을 설정 후 값을 입력하면 됨)
student["gpa"] = 4.3
print(student)

# 딕셔너리 삭제 (del 방법은 앞서 배웠지만 삭제되는 값이 반환이 안됨. 할거면 pop 같은 것을 사용)
del student["grade"]
print(student)