# Way 1 ------------------>>>>>>>>>>>>>>>>>>>>

factorial_lambda = lambda n: 1 if n == 0 or n == 1 else n * factorial_lambda(n-1)

# Way 2 ------------------>>>>>>>>>>>>>>>>>>>>

n=int(input("Enter a number:- "))
res=1
for i in range(n,1):
    res*=i
    
    
