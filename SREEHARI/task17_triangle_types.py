#17.WAP to check whether a triangle is Equilateral, Isosceles or Scalene

x=int(input("enter x value:"))
y=int(input("enter y value:"))
z=int(input("enter z value:"))
if x==y and y==z:
    print("this is Equilateral")
else:
    if x==y or y==z or z==x:
        print("this is Isosceles")
    else:
        print("this is Scalene")
