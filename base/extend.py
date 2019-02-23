# 继承
class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name + " is Studying")

    def intro(self):
        print("I am a student")


class Gradurate(Student):
    def __init__(self, name):
        super().__init__(name)
        self.category = "graduate"

    def intro(self):
        print("I am a " + self.category)


stu = Student("xiaoming")
stu.study()
stu.intro()

gradurate = Gradurate("xiaoming")
gradurate.study()
gradurate.intro()