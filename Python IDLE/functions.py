'''def add():
   sum= a+b+c+d
   return (sum)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
sum=add()
print("THE SUM:",sum)

def add():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    return(a+b+c+d)
print(add())

def volume():
    r=float(input())
    pi=3.14
    h=float(input())
    volumeofcone=(1/3)*pi*r**2*h
volume()'''

def cone():
    r=int(input())
    h=int(input())
    print("Cone:",1/3*3.14*r**2*h)
def swap(a,b):
    a,b=b,a
    print("After Swap:",a,b)
def rec(l,b):
    return(l*b)
def peri():
    a=int(input())
    b=int(input())
    return(2*(a+b))
cone()
swap(10,20)
print(rec(10,2))
print(peri())
