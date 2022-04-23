#8. WAP find largest of two numbers
n=int(input("enter 1st num:"))
n1=int(input("enter 2nd number:"))
if (n>n1 and n!=n1):
    print("max number is :",n)
else:
    if(n1>n):
        print("max number is:",n1)
    else:
        print("enter diff_numbers")
