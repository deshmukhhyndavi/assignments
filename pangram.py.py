#program to find whether a given string is pangram or not

string=input("enter the string")
alpha="abcdefghijklmnopqrstuvwxyz"
for char in alpha:
    if char not in string.lower():
        f=0
    else:
        f=1
if f==1:
    print("yes!it is pangram")
if f==0:
    print("no!it is not a pangram")
        
        
