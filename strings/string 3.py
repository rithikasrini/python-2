'''Write a Python function that takes a sentence and returns the longest word and the length of the longest one.'''
str1=input()
str2=str1.split()
print(str2)
str3=""
for i in str2:
    if(len(i)>len(str3)):
        str3=i
print(str3)
