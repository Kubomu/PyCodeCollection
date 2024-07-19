"""
Day.py
A program to display the day of the week

This program prompts the user to enter the year, month, and day of the month, and then calculates and displays the corresponding day of the week.

Example usage:

    $ python Day.py
    Enter day of the month(1-31): 25
    Enter the month(1-12): 12
    Enter the year of the century: 2022
    Friday

"""
q = eval(input("Enter day of the month(1-31): "))
m = eval(input("Enter the month(1-12): "))
k = eval(input("Enter the year of the century: "))
j = k/100
#Getting the value of h

h = int((q+ (26*(m + 1) / 10) + k + (k / 4) + (j / 4) + 5*j ) % 7)

#getting day of the week
if h==1:
    print("Monday")
    
elif h==2:
    print("Tuesday")
    
elif h==3:
    print("Wednesday")  
          
elif h==4:
    print("Thursday")
    
elif h==5:
    print("Friday")    
    
elif h==6:
    print("Saturday")
    
elif h==7:
    print("Sunday")        