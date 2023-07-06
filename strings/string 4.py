'''Write a Python function which finds the length of the string, if the length of the string is multiple of 5, reverse the string and capitalize all the characters.'''
str1=input()
str2=""
a=len(str1)
if(a%5==0):
    str2=str1[::-1]
    str2=str.upper(str2)
    print(str2)
