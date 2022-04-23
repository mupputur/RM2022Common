#23. Write a program in C which is a Menu-Driven Program to perform a simple calculation.

x=int(input("enter x value:"))
y=int(input("enter y value:"))
i=int(input("choose 1. addition, 2. subtraction, 3. multiplication, 4. division: "))
if i == 1 and i>0 and i<=4:
    print("1 Addition x+y:",x+y)
else:
    if i == 2 and i>0 and i<=4:
        print("2. Subtraction x-y:",x-y)
    else:
        if i == 3 and i>0 and i<=4:
            print("3. Multiplication x*y:", x * y)
        else:
            if i == 4 and i>0 and i <=4:
                print("4. division x%y:", x % y)
