# 7-9 딕셔너리 - 딕셔너리 정의 및 선언

# 딕셔너리는 중괄호로 선언
student = {
    "student_no" : "20231234",
    "major" : "English",
    "grade" : 1
}

# 대괄호에 키값을 넣어서 출력함 (여기서 키는 student_no, major, grade)
print(student["student_no"])

# 학번 데이터를 변경 후 출력
student["student_no"] = "202301235"

print(student)
print(student["student_no"])