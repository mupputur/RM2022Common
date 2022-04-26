##wap to accept a coordinate point in a xy coordinate system and dtermine in which
##quadrant the coordinate point lies.



x=3
y=4
cor=(x,y)
if (x,y)== cor:
    print ("it lies in 1st quadrant")
elif (-x,y)==cor:
    print("it lies in 2nd quadrant")
elif (-x,-y)==cor:
    print("it lies in 3rd quadrant")
elif (x,-y)==cor:
    print("it lies in 4th quadrant")
    

