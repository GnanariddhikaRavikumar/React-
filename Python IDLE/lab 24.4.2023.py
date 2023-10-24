#sum of n natural numbers
num=int(input())
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

#sum of digits
num=int(input())
sum=0
while(num!=0):
    n=int(num)%10
    sum=sum+n
    num=num/10
print(sum)

#no of digits
num=int(input())
sum=0
while(num!=0):
    sum=sum+1
    num=int(num/10)
print(sum)

#palindrome
num=int(input())
n=num
sum=0
while(num!=0):
    r=num%10
    sum=(sum*10)+(r)
    num=int(num/10)
print(sum)
if(n==sum):
    print(n,"is a Palindrome")
else:
    print(n,"is not a Palindrome")

#reverse the number
num=int(input())
n=num
sum=0
while(num!=0):
    r=num%10
    sum=(sum*10)+(r)
    num=int(num/10)
print(sum)'''
