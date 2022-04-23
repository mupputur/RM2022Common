"""14. WAP to find the eligibility of admission for a professional course based on the following criteria:
            Marks in Maths >=65
            Marks in Phy >=55
            Marks in Chem>=50
            Total in all three subject >=180
                     or
            Total in Math and Physics >=140"""

math = int(input("enter math marks:"))
phy = int(input("enter physics marks:"))
chem = int(input("enter chemistry marks:"))

if (math + phy + chem >= 180 or math + phy >= 140) and (math >= 65 and phy >= 55 and chem > 50):
    print("you are elisible for professional course")
else:
    print("not elisible for admission")
