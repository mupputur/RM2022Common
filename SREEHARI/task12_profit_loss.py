#12.WAP to calculate profit and loss on a transaction from the given cost price(cp) and selling price (SP)
cp=float(input("enter the cost_price:"))
sp=float(input("enter the selling_price:"))
if sp-cp>0 and sp>0 and cp>0:
     print("this transaction profitable:",sp-cp)
else:
     if sp-cp<0 and sp>0 and cp>0:
          print("this transaction loss:",sp-cp)
     else:
         if sp==cp and sp>0 and cp>0:
             print("enter sp and cp different values")
