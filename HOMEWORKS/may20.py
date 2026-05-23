present= int(input("Enter the amount of days you have been present: "))
absent= int(input("Enter the amount of days you have been absent: "))
total= present + absent
percentage= (present/total)*100
print("Your attendance percentage is: ", percentage, "%")
if percentage>=75:
    print("You are allowed to sit in the exam") 
else:    print("You are not allowed to sit in the exam")