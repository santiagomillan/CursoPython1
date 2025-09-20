class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi! I'm a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hi! I'm {self.name}, a student with ID {self.student_id}.")

# Example usage
student = Student("Alice", 31, "S12345")
student.greet()