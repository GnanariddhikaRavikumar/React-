'''squ=[x**2 for x in range(11)]
print(squ)
tup1=("CCE")
tup2=("CCE",)
tup3=(10,20,30)
tup4=(10,23,"CCE")
tup5=(10,23,(100,200,300),500)
print(type(tup1),type(tup2))
print(tup2,tup3,tup4)
print(id(tup2))
print(tup2[0],tup3[-1])
print(tup2*4)
print(tup2[::])
print(tup3[1:],tup3[:3],tup3[0:3])
print(tup3[0:5:2])
print(tup3[-3:-1:1])
print(tup3.count(10))

def swap(x,y):
    (x,y)=(y,x)
    return (x,y)
print(swap(10,20))'''

def circle(r):
    return(2*3.14*r,3.14*r**2)
    
print(circle(int(input("Enter Radius:"))))
