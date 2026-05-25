num1= int(input("Enter a number: "))
num2= int (input("Enter another number: "))
def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("The sum of", num1, "and", num2, "is", addition(num1,num2))
print("the differernce of", num1, "and", num2, "is", subtraction(num1,num2))
print("the product of", num1, "and", num2, "is", multiplication(num1,num2))
print("the quotient of", num1, "and", num2, "is", division(num1,num2))