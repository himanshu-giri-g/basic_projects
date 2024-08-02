# Way 1 ----------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a=int(input("Enter a Number:- "))
b=str(a)
c=len(b)
sum=0
for i in b:
    sum+= int(i)**c
if sum==a:
    print(f"The No. {a} is an Armstrong Numeber.")
else:
    print(f"The No. {a} is not an Armstrong Numeber.")

#Way 2 ----------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def arm_strong(n,x=None):
#     if x is None:
#         x=n
#         print(x)
#     if n==0:
#         return 0
#     y = n % 10

#     z = len(str(x))
#     print(z)
#     return y**z + arm_strong(n // 10,x)

# a=int(input("Enter a Number:-"))
# if arm_strong(a)==a:
#     print("The No. ",a," is an Armstrong Numeber.")
# else:
#     print("The No. ",a," is not an Armstrong Numeber.")

#Way 3 ----------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
