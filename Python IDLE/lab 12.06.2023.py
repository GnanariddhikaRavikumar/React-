'''
#factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*(fact(n-1))
n=int(input("Enter a Number:"))
print("Factioral:",fact(n))

#Area of circle and rectangle
def circle(r):
    return(3.14*r**2)
def rectangle(l,b):
    return(l*b)
r=int(input("Enter radius:"))
print("Area of Circle:",circle(r))
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
print("Area of Rectangle:",rectangle(l,b))

#Maximum of list
list=[1,2,3,4,56,78]
max=list[0]
for i in range(len(list)):
    if(max<list[i]):
        max=list[i]
print("Maximum element:",max)'''

#count
str=input("Enter a string:")
char=input("Entr character:")
count=0
for i in range(len(str)):
    if(char==str[i]):
        count+=1
    else:
        continue
if(count==0):
    print("not Found")
else:
    print("Found")
