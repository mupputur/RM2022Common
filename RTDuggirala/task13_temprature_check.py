
#WAP to find the weather condition

t=int(input('enter the temparature: '))

if t<0:
    print(t,'is a freezing temparature')
    
elif 10>=t>0:
    print(t,'is very cold temparature')

elif 20>=t>10:
    print(t,'is cold temparature')

elif 30>=t>20:
    print(t,'is a normal temparature')

elif 40>=t>30:
    print(t,'it is hot temparature')

elif t>40:
    print(t,'it is very hot temparature')
    
    
