# Way 1 ------------------>>>>>>>>>>>>>>>>>>>>

factorial_lambda = lambda n: 1 if n == 0 or n == 1 else n * factorial_lambda(n-1)

# Way 2 ------------------>>>>>>>>>>>>>>>>>>>>

# def factorial(num): 
#     if (num == 1 or num == 0):
#         return 1
#     else:
#         return (num * factorial(num - 1))
    
# num=int(input("Enter a number:- "))
# print(factorial(num))
    
# Way 3 ------------------>>>>>>>>>>>>>>>>>>>>
