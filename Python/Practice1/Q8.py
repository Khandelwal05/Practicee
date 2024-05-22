class NegativeNumber(Exception):
    "when negative number is entered"
    pass

try:
    num=int(input("Enter number here: "))
    if num<0:
        raise NegativeNumber 

except NegativeNumber:
    print("Negative No")

except Exception as e:
    print("Error",e)

else:
    i=num
    fact=1
    while(i>0):
        fact=fact*i
        i-=1

    print(fact)