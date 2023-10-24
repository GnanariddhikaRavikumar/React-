'''def fibo():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b;
f=fibo()
for i in range(10):
    print(next(f))'''

def fib(n):
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
