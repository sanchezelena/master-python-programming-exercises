# Your code here
class Student:
    def __init__(self, name, age, grade): # Estos son sus atributos
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self): # Esto es un método
        return f"Hello! I am {self.name}, I am {self.age} years old, and my current grade is {self.grade}."

    def study(self, hours): # Esto es otro método
        self.grade += hours * 0.5
        return f"After studying for {hours} hours, {self.name}'s new grade is {self.grade}."

student1 = Student("Elena", 25, 70)

print(student1.introduce())
print(student1.study(5))