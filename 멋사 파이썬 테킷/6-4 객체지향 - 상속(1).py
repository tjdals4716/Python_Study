# 10-4 객체지향 - 상속(1)

class Student:
    
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")

class ForeignStudent(Student):

    def __init__(self, name, major, country):
        super().__init__(name, major)
        #Student 클래스에는 없는 개체를 생성
        self.country = country

foreign_student_1 = ForeignStudent("외길동", "러시아어학과", "미국")
print(foreign_student_1.name)
print(foreign_student_1.major)
print(foreign_student_1.country)
print(foreign_student_1.is_graduated)