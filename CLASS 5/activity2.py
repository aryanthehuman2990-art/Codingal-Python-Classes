fact= int(input("Enter a number: "))
def factorial(n):
    if n==1:
        return 1
    else:
         return n*factorial(n-1)
if fact<0:
        print("factorial does not exist for negative numbers")
elif fact==0:
        print("the factorial of 0 is 1")
else:
        print("the factorial of", fact, "is", factorial(fact))