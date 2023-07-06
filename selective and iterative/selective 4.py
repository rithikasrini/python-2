a=int(input("enter first  number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if((a<b) and (b<c)):
    if(c*c == a*a + b*b):
        print("1")
    else:
        print("0")
