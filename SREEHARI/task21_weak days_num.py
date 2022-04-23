"""#21.	WAP to read any day number in integer and display day name in the word
Input:4    Expected Output: Thursday   """

day=int(input("enter the day number:"))
if day==1 and day>0 and day<=7:
    print("Monday", )
else:
    if day==2 and day>0 and day<=7:
        print("Tuesday", )
    else:
        if day==3 and day>0 and day<=7:
            print("Wednesday", )
        else:
            if day==4 and day>0 and day<=7:
                print("Thursday", )
            else:
                if day==5 and day>0 and day<=7:
                    print("Friday", )
                else:
                    if day==6 and day>0 and day<=7:
                        print("Saterday", )
                    else:
                        if day==7 and day>0 and day<=7:
                            print("Sunday", )
