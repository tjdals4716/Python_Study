# 10-3 객체지향 - 클래스(3)

class Student:
    
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f"{student_1.major}로 전공이 변경되었습니다.")

# 인스턴스 - 실체와된 사물

student_1 = Student("홍길동", "컴퓨터공학과")

# 학과데이터를 기계공학과로 새롭게 덮어씀(수정) 
# student_1.major = "기계공학과"

# 함수를 통해서 학과를 변경하는 방법
student_1.edit_major("기계공학과")
print(student_1.major)

student_1_name = student_1.name
print(student_1_name)

student_1_graduated = student_1.is_graduated
print(student_1_graduated)

student_1.study()