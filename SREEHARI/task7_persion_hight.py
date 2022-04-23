#7. WAP to accept the height of a person in centimeter and categorize the person according to their height. If the height is less than 150 display output as “DWARF” and if the height is greater than equal to 150 and less than 165 display output as “AVERAGE HEIGHT” and if the height is greater than 165 display output as “TALL”
h=int(input("enter your Height:"))
if h<150:
    print("you are DWARF")
else:
    if (h>150 and h<165):
        print("You are AVERAGE HEIGHT")
    else:
        print("You are TALL")
