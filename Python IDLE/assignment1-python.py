'''#tax calculation
apple=int(input("Enter the Quantity of apple:"))
c1=int(input("Enter the cost of apple:"))
banana=int(input("Enter the Quantity of banana:"))
c2=int(input("Enter the cost of banana:"))
orange=int(input("Enter the Quantity of orange:"))
c3=int(input("Enter the cost of orange:"))
total=((apple*c1)+(banana*c2)+(orange*c3))
print("Total Cost:",total+0.05)'''

'''#calculate
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=int(input("Enter the value of z:"))
w=int(input("Enter the value of w:"))
print((2+3)*(4-1)/2)
print((x>5)and(y<10)or(z==20))
print((x>5)and((y<10)or(z==20)))
print((x+y)*z>10 and (w%3)==0)
print((x+y)*z>10 or(w%3)==0and(a!=b))'''

'''pas=input("Enter a password:")
l=len(pas)
count=0
if(l<6):
    print("Enter valid password")
else:
    for i in range(l):
        if((ord(pas[i])>=33 and ord(pas[i])<65) or (ord(pas[i])>=91 and ord(pas[i])<97) or (ord(pas[i])>=123 and ord(pas[i])<127)):
            count+=1
        if(pas[i]==" "):
            print("Space are not allowed")
        if(count>1):
            break;
'''
dict=eval(input())
print(dict)

    

           
        
