class Calculator:
    def __init__(self, marks):
        self.marks=marks
    def grades(self):
        if (self.marks >=90 and self.marks <=100):
            print("A")
        elif (self.marks >80 and self.marks <=89):
            print("B")
        elif (self.marks >=70 and self.marks <=79):
            print("C")
        elif (self.marks >=60 and self.marks <=69):
            print("D")
        elif (self.marks >=0 and self.marks <=59):
            print("F")
C1=Calculator(29)
C1.grades()