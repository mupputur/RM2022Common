#10. WAP to check whether a character is an alphabet, digit or special character.
str = str(input("enter the char:"))
if (str>='a'and str<='z'):
    print("this is lower alphabets:", str)
else:
    if (str >= 'A' and str <= 'Z'):
        print("this is upper alphabets:", str)
    else:
        if (str>='0'and str<= '9'):
            print("this is disits:", str)
        else:
            print("this is special simble")
