'''Write a Python program to display a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample Input
Property
Sample Output
Prty'''

str1=input()
str2=str1[0:2]
str3=str1[-2:]
str4=str2+str3
print(str4)
