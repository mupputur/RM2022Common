
#20. WAP to accept a grade and declare the equivalent description


grade = str(input("enter E,V,G,A,F grade:"))
if grade == 'E':
    print("Excellent:", )
else:
    if grade == 'V':
        print("Very good")
    else:
        if grade == 'G':
            print("Good")
        else:
            if grade == 'A':
                print("Average")
            else:
                if grade == 'F':
                    print("Fail")
