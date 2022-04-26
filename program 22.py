##WAP to read anu month number in integer and display the how many days in
##this month.

month= int(input("enter month:"))
year=int(input("enter year:" ))
if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("number of days is 31")
elif month==2 and year%4==0:
    print("Number of days is 29")
elif month==2:
    print("Number of days is 28")
else:
    print("Number of days is 30")
