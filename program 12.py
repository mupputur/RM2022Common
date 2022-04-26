## WAP a accept to calucalate the profit or loss

cp=int(input("enter cost  price: "))
sp=int(input("enter selling price: "))
if cp==sp:
    print("no profit and no loss")
elif cp<sp:
    print("profit", sp-cp)
else:
    print("loss", cp-sp)
