
#WAP to find which type of triangle

a=int(input('enter the 1st side : '))
b=int(input('enter the 2nd side : '))
c=int(input('enter the 3rd side : '))

if a==b==c:
    print('this is eqilateral triangle')

elif a==b or b==c or c==a :
    print('this is the isosceles triangle')

else:
    print('this is the scalene triangle')
