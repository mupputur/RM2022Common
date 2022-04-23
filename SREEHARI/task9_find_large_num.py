#9. WAP to find the largest of three numbers.
n=int(input("enter 1st num:"))
n1=int(input("enter 2nd number:"))
n2=int(input("enter 3nd number:"))
if (n>n1 and n>n2) and (n!=n1 and n1!=n2):
    print("max number is :",n)
else:
    if(n1>n and n1>n2 and n!=n1 and n1!=n2):
        print("max number is:",n1)
    else:
        if(n2>n and n2>n1 and n!=n1 and n1!=n2):
            print("max number is:",n2)
        else:
            print("please enter different values")
