year=int(input("enter year:"))
fare=1020
conc=0
if((2023-year)>60):
    conc=fare-(1020*10/100)
    print("the concession is:",conc)
else:
    print("the original fare is:",fare)
