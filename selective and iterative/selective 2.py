a=int(input("enter first side of a triangle:"))
b=int(input("enter second side of a triangle:"))
c=int(input("enter third side of a triangle:"))
if(((a+c)>b) and((a+b)>c) and ((b+c)>a)):
    print("the triange is possible")
else:
    print("the triange is not possible")
