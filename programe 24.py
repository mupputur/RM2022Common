## Wap to menu driven program to capture the area of a circle, square and rectangle


print("Menu Driven Program")
print("1. Area of Cricle")
print("2. Area of Rectangle")
print("3. Area of square")
choice=int(input("Enter your choice:" ))
if choice==1:
    radius=int(input("enter radius of circle:"))
    print("Area of Circle", 3.14*radius*radius)
elif choice==2:
    length=int(input("enter length of rectangle:"))
    breadth=int(input("enter breadth of rectangle:"))
    print("Area of Rectangle", length*breadth)
elif choice==3:
    side=int(input("enter side of square:"))
    print("Area of square", side*side)
else:
    print("Wrong choice")
