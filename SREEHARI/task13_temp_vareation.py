"""13 WAP to read temperature in centigrade and display a suitable message according to temperature state below
    Temp < 0 then Freezing weather
    Temp 0-10 then Very Cold weather
    Temp 10-20 then Cold weather
    Temp 20-30 then Normal in Temp
    Temp 30-40 then Its Hot
    Temp >=40 then Its Very Hot"""

tem=int(input("enter temparature value:"))
if tem<0:
     print("this is frezing weather:",tem)
else:
     if tem>=0 and tem<10:
          print("this is very cold weather:",tem)
     else:
          if tem>=10 and tem<20:
               print("this is cool weather:",tem)
          else:
               if tem>=20 and tem<30:
                    print("this is normal tempareture:",tem)
               else:
                    if tem>=30 and tem<40:
                         print("this is hot :",tem)
                    else:
                         if tem>=40:
                              print("this is very hot:",tem)
