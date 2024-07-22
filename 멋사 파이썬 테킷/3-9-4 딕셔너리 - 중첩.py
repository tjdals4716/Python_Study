# 7-13 딕셔너리 - 중첩
# 이 부분 강의 한 번 더 보기

student_1 = {
    "student_no" : "1",
    "gpa" : "4.3"
}

student_2 = {
    "student_no" : "2",
    "gpa" : "3.8"
}

# students 함수를 선언 후 리스트 형식으로 배열하면 됨
students = [student_1, student_2]

# 입력한 키에 대한 값을 출력
for student in students:
    print(student['student_no'])

# 키에 graduted를 추가
for student in students:
    student['graduted'] = False
    print(student)

# 새롭게 선언해줌 (위랑 관련 X)
student = {
    "subjects" : ["운영체제", "데이터베이스", "컴퓨터네트워크"]
}

print(student["subjects"])

subject_list = student["subjects"]

for subject in subject_list:
    print(subject)

# 새롭게 선언해줌 (위랑 관련 X)
student_3 = {
    "scholarship" : {
        "name" : "국가장학금",
        "amount" : "100000"
    }
}

print(student_3)

# 키에 대한 데이터를 확인
for key in student_3.keys():
    print(key)

# 값에 대한 데이터를 확인
for value in student_3.values():
    print(value)

# 값에 대한 이중 for문으로 데이터를 확인
for value in student_3.values():
    for value_2 in value.values():
        print(value_2)