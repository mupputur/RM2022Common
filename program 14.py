Ma=int(input("enter marks of the maths: "))
py=int(input("enter marks of the physics: "))
ch=int(input("enter marks of the chemistry: "))
total=Ma+py+ch
sub=Ma+py    
if total>=180 or sub>=140:
    print("eligible for admission")
else:
    print("not eligible for admission")
    
