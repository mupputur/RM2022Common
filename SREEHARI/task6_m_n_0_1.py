#6. WAP to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0.
m=int(input("enter m value:") )
if m>0:
   n=1
   print("n:",n)
else:
    if m==0:
        n=0
        print("n:",n)
    else:
        n=-1
        print("n:",n)
