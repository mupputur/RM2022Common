
#WAP to find the which quadrants are given point

x=int(input('enter the x value : '))
y=int(input('enter the y value : '))

if x>=0 and y>=0:
    print('this vertex belongs to 1st quadrant')

elif x<0 and y>=0:
    print('this vertex belongs to 2nd qudrant')

elif x>=0 and y<0:
    print('this vertex belongs to 4th quadrant')
else:
    print('this vertex belongs to 3rd quadrant')
