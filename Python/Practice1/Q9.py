string=str(input())
s1=[]
l=len(string)-1
for i in range(l,-1, -1):
    s1.append(string[i])
a="".join(s1)
print(a)
if (string==a):
    print("Yes")
else :
    print("No")