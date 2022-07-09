# 18. WAP to find a triangle values valid or invalid 

x=int(input('enter the 1st angle :'))
y=int(input('enter the 2nd angle : '))
z=int(input('enter the 3rd angle : '))

total=x+y+z

if total==180:
    print('this is a valid triangle')

else :
    print('this is an invalid triangle')
