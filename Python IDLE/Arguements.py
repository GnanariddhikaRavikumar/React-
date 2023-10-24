'''def sum(n1=10,n2=300):
    print(n1+n2)
sum(10,20)      #default arguement
sum(100)        #default arguement
sum(n1=25)      #keyword arguement
sum(n2=100)     #keyword arguement   
sum(n1=20,)
#sum(n2=100,10) #positional arguement follows keyword arguement
sum(n1=10,)'''

def disp(n1,n2,name="SECE"):
    print(n1,n2,name)
disp(10,20.3)
disp(10,20.3,)
disp(n2=20.3,n1=100)
disp(n2=20.3,n1=100,)
#disp(n2=20.3,n1=100,"CCE")  #positional arguement follows keyword arguement
disp(n2=20.3,name="CCE")        #required arguement
disp(n2=20.3,n1=100,name="CCE")

'''global sum
def prod(a=[1,2,3,50]):
    sum=1
    for i in a:
        sum=sum*i
        return sum
print('''


