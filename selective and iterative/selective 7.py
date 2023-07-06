sal=int(input("enter salary:"))
year=int(input("enter service:"))
bonus=0
if(year>10):
    bonus=sal*10/100
    print("the bonus:",bonus)
if((year>6) and (year<10)):
    bonus=sal*8/100
    print("the bonus:",bonus)
if(year<6):
    bonus=sal*5/100
    print("the bonus:",bonus)
