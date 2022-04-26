
##  WAP to find the largest of three numbers

"""
x=10
y=20
z=30
if x<y and y<z:
    print("y,z are the largest number than x")
elif x<z and z<y:
    print("x,z are the largest numbers than y")
else:
    print("y is largest numbers")
"""

def largest_number(x,y,z):
    if x<y and y<z:
        print("y,z are the largest number than x")
    elif x<z and z<y:
        print("x,z are the largest numbers than y")
    else:
        print("y is largest numbers")
largest_number(10,20,30)    
