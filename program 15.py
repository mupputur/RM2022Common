## wap to read the roll number , sname,marks of three subjects. caluclate the
##total, percentage, division.



n= input("enter roll number:" )
m=input("enter name:" )
x=int(input("enter marks m1:" ))
y=int(input("enter marks m2:" ))
z=int(input("enter marks m3:" ))
t=x+y+z
a=t/3
per=((x+y+z)/300*100)
print("total", t )
print("avg", a)
if per>=60:
    print("the division is first")
elif (per<60)and (per>=48):
    print("the divisiion is second")
elif (per<48)and (per>=38):
    print("the division is pass")
elif per<36:
    print("the division is fail")
    

 
        
    
