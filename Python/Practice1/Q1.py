class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print("make is", self.make)
        print("model is", self.model)
        print("year is", self.year)
C1=Car('abc',123,2022)
C1.display_info()
