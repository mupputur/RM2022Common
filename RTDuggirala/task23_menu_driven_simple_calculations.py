# WAP to menu driven program for simple calculations

print('''         1.addition
         2.subtraction
         3.multiplication
         4.division
         5.exit''')
s=int(input('select the operation : '))

x=int(input('enter the 1st value : '))

y=int(input('enter the 2nd value : '))

if s==1:
   t= x+y
   print(t,'here is the edition') 
