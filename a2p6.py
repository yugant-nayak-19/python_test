#problem 6
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num = 8
if num<0:
    print("factorial does not exist")
elif num==0:
    print("factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))
