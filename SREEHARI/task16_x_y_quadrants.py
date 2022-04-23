#16. Write a C program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.

x=int(input("enter x value:"))
y=int(input("enter y value:"))
if(x>=0 and y>=0):
    print("this is 1st Quadrant")
else:
    if(x<0 and y>=0):
        print("this is 2nd Quadrant")
    else:
        if(x<0 and y<0):
            print("this is 3ed Quadrant")
        else:
            if(x>=0 and y<0):
                print("this is 4th Quadrant")
