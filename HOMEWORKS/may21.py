x=int(input("Enter a number: "))
if x>=1 and x<=10:
    print("the number is an armstrong number")
elif x>10 and x<100:
    no1=str(x)[0]
    no2=str(x)[1]
    if int(no1)**2+int(no2)**2==x:
        print("the number is an armstrong number")
    else:        print("the number is not an armstrong number")
elif x>=100 and x<1000:
    no1=str(x)[0]
    no2=str(x)[1]
    no3=str(x)[2]
    if int(no1)**3+int(no2)**3+int(no3)**3==x:
        print("the number is an armstrong number")
    else:
        print("the number is not an armstrong number")

    