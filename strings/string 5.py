'''Write a python program which reads your mail id, and extract the username from the mail id and generate the password such as username and the reverse of it.
Sample Input
Enter the email id: bvishnu2731@gmail.com
Sample Output
Username - bvishnu2731
Password - bvishnu27311372UNHSIVB
The username is the first part of the Gmail address, before the @ symbol. 
Password will be the combination of username followed by the reverse uppercase of the username.'''
str1=input("enter email:")
str2=""
for i in str1:
    if(i=='@'):
        break
    else:
        str2+=i
str3=str2[::-1]
print(str2)
str3=str.upper(str3)
print(str2+str3)
