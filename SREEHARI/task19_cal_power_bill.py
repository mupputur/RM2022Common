#19 WAP to calculate and print the Electricity bill of a given customer. The customer id., name and unit consumed by the user should be taken from the keyboard and display the total amount to pay to the customer. The charge is as follow:

u=float(input("enter units:"))
bill=u*1.20
if u>=0 and u<=199:
    print("the total amount is:",bill)
else:
    bill=u*1.50
    if u>=200 and u < 400:
        print("the total amount is:", bill)
    else:
        bill = u * 1.80
        if  u>=400 and u < 600:
            print("the total amount is:", bill)
        else:
            u * 2.0 == bill
            if u >=600:
                print("the total amount is:", bill)


