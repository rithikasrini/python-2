'''Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample Input
Mike
Dice
Sample Output
Dike
Mice'''
str1=input()
str2=input()
str3=str2[0:1]+str1[1:]
str4=str1[0:1]+str2[1:]
print(str3)
print(str4)
