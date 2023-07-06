for i in range(1,10):
    co=1
    if i>1:
         for j in range(2,i):
            if(i%j==0):
               co=0
               break
         if(co==1):
            print(i)
