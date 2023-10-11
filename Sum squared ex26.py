n=int(input("type the number :"))
a=1
s=0
for i in range(1,n+1) :
    s=s+(a**2)
    a=a+2
print("the sum of squares is :",s)
