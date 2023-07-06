name=input("enter name:")
age=int(input("enter age:"))
gender=input("enter M or F:")
days=int(input("enter no of  days:"))
wages=0
if((age>=18) and (age<30) and gender=='M'):
        wages=700*days
        print("the wages:",wages)
if((age>=18) and (age<30) and gender=='F'):
        wages=750*days
        print("the wages:",wages)
if((age>=30) and (age<40) and gender=='M'):
        wages=800*days
        print("the wages:",wages)
if((age>=30) and (age<40) and gender=='F'):
        wages=800*days
        print("the wages:",wages)
