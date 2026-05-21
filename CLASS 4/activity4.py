x=int(input("Enter a number: "))
y=0
if x>=1:
    for i in range(1, x+1):
        if x%i==0:
            y+=1
    if y==2:
        print("the number is a prime number")
    else:
        print("the number is not a prime number")