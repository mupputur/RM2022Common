#22. WAP to read any Month Number in integer and display the number of days for this month.
month=int(input("enter month:"))
if month==1 and month>0 and month<=12:
    print("January in 31 days")
else:
    if month==2 and month>0 and month <=12:
        print("Feb in 28 days")
    else:
        if month==3 and month > 0 and month <= 12:
            print("March in 31 days")
        else:
            if month == 4 and month > 0 and month <= 12:
                print("April in 30 days")
            else:
                if month == 5 and month > 0 and month <= 12:
                    print("May in 31 days")
                else:
                    if month == 6 and month > 0 and month <= 12:
                        print("Jun in 30 days")
                    else:
                        if month == 7 and month > 0 and month <= 12:
                            print("July in 31 days")
                        else:
                            if month == 8 and month > 0 and month <= 12:
                                print("August in 31 days")
                            else:
                                if month == 9 and month > 0 and month <= 12:
                                    print("September in 30 days")
                                else:
                                    if month == 10 and month > 0 and month <= 12:
                                        print("October in 31 days")
                                    else:
                                        if month ==11 and month > 0 and month <= 12:
                                            print("November in 30 days")
                                        else:
                                            if month == 12 and month > 0 and month <= 12:
                                                print("December in 31 days")
