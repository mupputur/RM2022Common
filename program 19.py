cn=input("enter cnumber:" )
cname=input("enter cname :" )
unit= int(input("enter units:" ))
if unit<199:
    print("charge is 1.20")
elif unit>=200 and unit<400:
    print("charge is 1.50")
elif unit>=400 and unit<600:
    print("charge is 1.80")
elif unit>600:
    print("charge is 2.00")
