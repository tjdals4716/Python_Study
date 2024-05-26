# 10-1 객체지향 - 클래스(1)

class Student:
    
    def __init__(self, name, major, is_graduated):
        self.name = name
        self.major = major
        self.is_graduated = is_graduated

    def study(self):
        print(f"{self.name} 학생은 공부 중입니다.")