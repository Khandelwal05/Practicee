import random
r=random.randint(0,100)
# print(r)

while (True):
    choice=int(input("Enter any no guessed by u here"))
    if (choice <r-20):
        print("Too low")
    elif (choice>r-20 and choice <r):
        print("low")
    elif (choice > r+20):
        print("too high")
    elif (choice<r+20 and choice >r):
        print("high")
    else :
        print("correct")
        break
