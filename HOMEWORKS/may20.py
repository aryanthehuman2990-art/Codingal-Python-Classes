present= int(input("Enter the amount of days you have been present: "))
absent= int(input("Enter the amount of days you have been absent: "))
total= present + absent
percentage= (present/total)*100
print("Your attendance percentage is: ", percentage, "%")