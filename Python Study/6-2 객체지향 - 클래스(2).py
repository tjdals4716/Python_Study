# 10-2 객체지향 - 클래스(2)

class Student:
    
    def __init__(self, name, major, is_graduated):
        self.name = name
        self.major = major
        self.is_graduated = is_graduated

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

# 인스턴스 - 실체와된 사물
        
student_1 = Student("홍길동", "컴퓨터공학과", False)

# student_1_name = student_1.name
# print(student_1_name)

student_1.study()