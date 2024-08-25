class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check(self):
        if self.age > 60:
            return True
        else:
            return False


teacher1 = Teacher("Ram", 21)


print(teacher1.check())  













