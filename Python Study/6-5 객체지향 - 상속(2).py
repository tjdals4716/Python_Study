# 10-5 객체지향 - 상속(2)

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

    # 오버라이딩 : 부모클래스에 있는 것을 자식클래스에서 덮어씌운것
    def study(self):
        print(f"{self.name} is studying now.")

foreign_student_1 = ForeignStudent("외길동", "러시아어학과", "미국")
foreign_student_1.study()
# print(foreign_student_1.name)
# print(foreign_student_1.major)
# print(foreign_student_1.country)
# print(foreign_student_1.is_graduated)