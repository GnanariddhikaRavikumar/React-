#volume of cone,cylinder and sphere
def cone(r,h):
    vol=1/3*3.14*r**2*h
    print("VOLUME OF CONE:",vol)
def cylinder(r,h):
    vol=3.14*r**2*h
    print("VOLUME OF CYLINDER:",vol)
def sphere(r):
    vol=4/3*3.14*r**3
    print("VOLUME OF SPHERE:",vol)
r=int(input("Enter radius:"))
h=int(input("Enter Height:"))
cone(r,h)
cylinder(r,h)
sphere(r)

#fibonacci series
def fibo():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b
f=fibo()
print("FIBONACCI SERIES\n")
for i in range(50):
    print(next(f))

#ASCII Value of a character
str=input()
for i in str:
    print(i,ord(i))

#count the charcters
str=input()
upr=0
lwr=0
digits=0
vow=0
cons=0
sp=0
let="aeiouAEIOU"
s=len(str)
for i in str:
    if(i>='A' and i<='Z'):
        upr+=1
    elif(i>='a' and i<='z'):
        lwr+=1
    elif(i>='0' and i<='9'):
        digits+=1
    if i in let:
        vow+=1
    if i==" ":
        sp+=1
print("Upper",upr,"\nLower",lwr,"\ndigits",digits,"\nVowels",vow,"\nSpaces",sp,"\nWords",sp+1,"\nConsanants",s-(vow+sp+digits))
    
          



    
