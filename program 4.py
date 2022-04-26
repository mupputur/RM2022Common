## WAP to accept a given number is leap year or not


"""a=201
if a%4==0:
    print("given year is leap year")
else:
    print("not leap year")


s=int(input("\n enter any year: "))
if s%4==0:
    print("\n given year is leap year")
elif s%4!=0:
    print("\n given year is not leap year")
else:
    print("\n enter any year: ")


"""

def leap_year(s):
    if s%4==0:
        print("\n given year is leap year")
    elif s%4!=0:
        print("\n given year is not leap year")
    else:
        print("\n enter any year: ")
leap_year(2020)
        
