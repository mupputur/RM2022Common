
# 19.WAP to find electricity bill

n=str(input('enter the name of the customer : '))

u=int(input('enter the units : '))

if (0>u<=199):
    pa=u*1.2     #pa= payable amount

    print(pa,'is to be paid by',n)
    
elif (200>=u and u<400):
    pa=u*1.5

    print(pa,'is to be paid by',n)

elif (400>=u and u<600):
    pa=u*1.8
    print(pa,'is to be paid by',n)

else:
    pa=u*2
    print(pa,'is to be paid by',n)
