food_rating=int(input("enter food rating:"))
serv_rating=int(input("enter service rating:"))
amb_rating=int(input("enter ambience rating:"))
bill_amt=int(input("enter bill amount:"))
tips=0
if((food_rating==4) or (food_rating==5)):
    if((serv_rating==(4 or 5)) and (amb_rating==(4 or 5))):
        tips=bill_amt*10/100
        print("the tips is:",tips)
    else:
        tips=bill_amt*5/100
        print("the tips is:",tips)
if((food_rating==1) or (food_rating==2) or (food_rating==3)):
    if((serv_rating==(4 or 5)) and (amb_rating==(4 or 5))):
        tips=bill_amt*5/100
        print("the tips is:",tips)
    else:
        tips=bill_amt*1/100
        print("the tips is:",tips)
    
