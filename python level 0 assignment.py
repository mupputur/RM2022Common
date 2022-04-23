#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 1
x = int(input("Enter a value: "))
y = int(input("Enter a value: "))
if x == y:
    print("equal")
else:
    print("not equal")


# In[11]:


## 2
x = int(input("Enter a value: "))
if x%2 == 0 :
    print("Even")
else:
    print("odd")


# In[13]:


## 3
x = int(input("Enter a value: "))
if x > 0 :
    print("positive")
else:
    print("negative")


# In[8]:


## 4
x = int(input("Enter a year:"))
if x % 4 == 0:
    print("Leap year")
else:
    print("Non Leap year")


# In[2]:


## 5
x = int(input("Enter an age: "))
if x >= 18 :
    print("Eligible for vote ")
else:
    print("Under age")


# In[28]:


## 6 
m = int(input("Enter a number: "))
if m > 0:
    print("n = 1")
elif m == 0:
    print("n = 0")
elif m < 0:
    print("n = -1")


# In[14]:


## 7
height = int(input("Enter a height: "))
if height < 150:
    print("DWARF")
elif ((height >= 150) and (height < 165)):
    print("AVERAGE HEIGHT")
elif height >= 165:
    print("TALL")


# In[34]:


## 8
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x > y:
    print("X is greater")
else:
    print("Y is greater")


# In[35]:


## 9 
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
if ((x >= y) and (x >= z)):
    print("x is greater")
elif ((y >= x) and (y >= z)):
    print("y is greater")
else:
    print("z is greater")


# In[42]:


## 10
x = input("Enter a input : ")
 
if((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')): 
    print("x is an Alphabet") 
elif((x >= '0') and (x <= '9')):
    print("x is a Digit")
else:
    print("x is a Special Character")


# In[44]:


## 11
X = input("Enter an alphabet: ")
if ((x == 'a') or (x == 'A') or (x == 'e') or(x == 'E') or (x == 'i') or (x == 'I') or(x == 'o') or (x == 'O') or (x == 'u') or (x == 'U')):
    print("x is an vowel")
else:
    print("x is an consonant")


# In[47]:


## 12
sp = float(input("Enter a selling price:"))
cp = float(input("Enter a cost price:"))
if sp > cp:
    print("profit is ", sp-cp)
else:
    print("loss is", cp-sp)


# In[53]:


## 13
x = float(input("Enter a temperature: "))
if x < 0 :
    print("Freezing weather")
elif (x > 0 and (x <10)):
    print("Very Cold weather")
elif ((x > 10) and (x < 20)):
    print("Cold weather")
elif ((x >20) and (x < 30)):
    print("Normal in Temp")
elif ((x >30) and(x < 40)):
    print("Its Hot")
elif x >= 40:
    print("Its Very Hot")


# In[58]:


## 14
x = int(input("Enter marks in maths: "))
y = int(input("Enter marks in physics: "))
z = int(input("Enter marks in chemistry: "))
if ((x >= 65) and (y >= 55) and (z >= 50) and (x + y + z >= 180)):
    print("Eligible for admission")
else:
    print("not eligible")


# In[65]:


## 15
rollno = int(input("Enter roll no: "))
name = input("Enter name: ")
x = int(input("Enter 1st sub marks: "))
y = int(input("Enter 2nd sub marks: "))
z = int(input("Enter 3rd sub marks: "))
total = x+y+z
print(total)
per = (total/300)*100
print(per)
if per >= 60:
    print("First class")
elif ((per < 60) and (per >= 48)):
    print("Second class")
elif ((per < 48) and (per >= 36)):
    print("Third class")
elif per < 36:
    print("Fail")


# In[103]:


## 16
x = int(input("Enter a value: "))
y = int(input("Enter a value: "))
if x > 0 and y > 0:
    print("(x,y) lies in first quadrant")
elif x < 0 and y > 0:
    print("(x,y) lies in second quadrant")
elif x < 0 and y < 0:
    print("(x,y) lies in third quadrant")
elif x > 0 and y < 0:
    print("(x,y) lies in fourth quadrant")


# In[72]:


## 17
a = int(input("enter 1st angle of triangle: "))
b = int(input("Enter 2nd angle of triangle: "))
c = int(input("Enter 3rd angle of triangle: "))
if a == c:
    print("isosceles triangle")
elif a == b == c:
    print("Equilateral triangle")
elif (a<b or a>b or b>c or b<c):
    print("scalene triangle")


# In[73]:


## 18
a = int(input("enter 1st angle of triangle: "))
b = int(input("Enter 2nd angle of triangle: "))
c = int(input("Enter 3rd angle of triangle: "))
if a+b+c >= 180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")


# In[75]:


## 19
customer_id = int(input("Enter id:"))
name = input("Enter name:")
units = int(input("Enter no of units consumed: "))
if units <= 199:
    print("The total amount to pay is ", units*1.20)
elif units > 200 and units < 400:
    print("The total amount to pay is ", units*1.50)
elif units > 400 and units < 600:
    print("The total amount to pay is ", units*1.80)
elif units > 600:
    print("The total amount to pay is ", units*2.00)


# In[11]:


## 20
x = input("Enter a grade:")
if x == 'e':
    print("Excellent")
elif x == 'v':
    print("Very good")
elif x == 'g':
    print("Good")
elif x == 'a':
    print("Average")
elif x == 'f':
    print("Fail")


# In[96]:


## 21
x = int(input("enter a number (1-7):"))
if x == 1:
    print("Monday")
elif x == 2:
    print("Tuesday")
elif x == 3:
    print("Wednessday")
elif x == 4:
    print("Thursday")
elif x == 5:
    print("Friday")
elif x == 6:
    print("Saturday")
elif x == 7:
    print("Sunday")


# In[100]:


## 22
x = int(input("enter a number (1-12):"))
if x == 1:
    print("january it has 31 days")
elif x == 2:
    print("February has 28 days")
elif x == 3:
    print("march has 31 days")
elif x == 4:
    print("april has 30 days")
elif x == 5:
    print("may has 31 days")
elif x == 6:
    print("june has 30 days")
elif x == 7:
    print("july has 31 days")
elif x == 8:
    print("august has 31 days")
elif x == 9:
    print("september has 30 days")
elif x == 10:
    print("october has 31 days")
elif x == 11:
    print("november has 30 days")
elif x == 12:
    print("december has 31 days")


# In[4]:


## 23
x = int(input("Enter a number; "))

def addition(a,b):
    sum = a+b
    print(sum)
    
def subtraction(a,b):
    difference = a - b
    print(difference)
    
def multiplication(a,b):
    product = a * b
    print(product)
    
def division(a,b):
    division = a/b
    print(division)

if x == 1:
    print("addition")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    addition(a,b)
elif x == 2:
    print("subtraction")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    subtraction(a,b)
elif x == 3:
    print("multiplication")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    multiplication(a,b)
elif x == 4:
    print("division")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    division(a,b)
else:
    print(not valid)


# In[1]:


## 24
x = int(input("Enter a number; "))
def circle(radius):
    area = 3.14 * radius * radius
    print("Area of circle",area)
def rectangle(height,width):
    area = height * width
    print("Area of rectangle",area)
def triangle(base,height):
    area = 0.5 * base * height
    print("Area of triangle",area)
    
if x == 1:
    print("circle")
    radius = int(input("Enter radius of circle: "))
    circle(radius)
elif x == 2:
    print("rectangle")
    height = int(input("Enter height of rectangle: "))
    width = int(input("Enter width of rectangle: "))
    rectangle(height,width)
elif x == 3:
    print("triangle")
    base = int(input("Enter base of a triangle: "))
    height = int(input("Enter height of triangle: "))
    triangle(base,height)
else:
    print(not valid)


# In[ ]:




