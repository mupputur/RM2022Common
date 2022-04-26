##WAP to check whether a triangle is equilateral,isoceles triangle or scalene.


a=int(input("enter a value:" ))
b=int(input("enter b value:" ))
c=int(input("enter c value:" ))
if a==b==c:
    print("It is an eqilateral triange")
elif a==b or b==c or c==a:
    print("Its isosclese triangle")
else:
    print("Its scalene triangle")
