class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args   
        self.details = kwargs 

    def show_employee(self):
        print(f"Employee Name: {self.name}")
        print("Skills:", self.skills)
        print("Details:", self.details)
        
employee = Employee("John", "Python", "Django", age=30, department="IT")
employee.show_employee()