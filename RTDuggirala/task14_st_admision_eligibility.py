# WAP the eligibility criteria for admision

m=int(input('enter marks in maths: '))
p=int(input('enter marks in physics: '))
c=int(input('enter marks in chemistry: '))

if (m>=65 or p>=55 or c>=50) and (m+p+c)>=180:
    print('he/she is eligible for a professional course')

elif (m+p)>=140:
    print('he/she is eligible for a professional course')

else:
    print('he/she is not eligible for a professional course')
