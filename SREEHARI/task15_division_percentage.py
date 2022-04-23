"""15. WAP to read roll no, name and marks of three subjects and calculate the total, percentage and division.
             Per>= 60 then the division is “First";
             per<60 and per>=48 then the division is  "Second"
             per<48 and per>=36  then the division is  "Pass"
             per < 36	Then the division is "Fail".        """

roll=int(input("enter your rool number:"))
name=str(input("enter your name:"))
math=int(input("enter math marks:"))
phy=int(input("enter phy marks:"))
chem=int(input("enter chemistry marks:"))
t=math+phy+chem
p=(t*100)/300

if p>=60:
    print("the 1st division is:",p)
else:
    if(p>=48 and p<60):
        print("the division is Second:",p)
    else:
        if(p>=36 and p<46):
            print("the division is Pass:",p)
        else:
            if(p<36):
                print("the division is Fail:",p)
