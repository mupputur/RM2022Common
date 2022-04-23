#24.	WAP which is a Menu-Driven Program to compute the area of the various geometrical shape.


r=int(input("enter r value:"))
length=int(input("enter length value:"))
width=int(input("enter width value:"))
base=int(input("enter base value:"))
height=int(input("enter height value:"))
i=int(input("choose option 1.area_circle,2.area_rectangle, 3.area:"))
if(i==1 and i!=2 and i!=3) and r>0 :
    print("the output is aria_circle:",3.1415*(r*r))
else:
    if(i==2 and i!=1 and i!=3)and length>0 and width>0:
        print("the out put is area_rectangle:", length*width)
    else:
        if(i==3 and i!=1 and i!=2)and base>0 and height>0:
            print("the output is area:",0.5*base*height)
