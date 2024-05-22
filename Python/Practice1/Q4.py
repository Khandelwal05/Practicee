class Employee:
    def __init__(self, name , age , salary ):
        self.name=name
        self.age=age
        self.salary=salary
    def display_info(self):
        print("Employee's name is ",self.name)
        print("Employee's age is ",self.age)
        print("Employee's salary is ",self.salary)


E1=Employee("Riya",21,5000)
E1.display_info()