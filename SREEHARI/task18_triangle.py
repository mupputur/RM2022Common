"""#18.	WAP to check whether a triangle can be formed by the given value for the angles
Hint: The triangle will be possible if sum of all angles must be equal to 180"""

x=int(input("enter x angle:"))
y=int(input("enter y angle:"))
z=int(input("enter z angle:"))
if x+y+z==180:
    print("this is Triangle")
else:
    print("this is not triangle")
