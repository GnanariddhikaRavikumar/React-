'''str=input("Enter String:")
str1=str[::-1]
if(str==str1):
    print("PALINDROME")
else:
    print("NOT A PALINDROME")'''


str1=input("Enter String:")
str2=""
l=len(str1)
for i in range(l):
    if(str1[i]>="A" and str1[i]<="Z")or(str1[i]>="a" and str1[i]<="z"):
        str1.replace("$",str1)
    else:
        str2[i]=str1[i]
print(str1)
