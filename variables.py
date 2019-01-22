# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:14:33 2019

@author: aWX614523
"""

__author__ = "xabidas"
#Below shows all the valid declarations of varibales in Python 
greeting="Bruce"
_myName="Abinash Dash"
Tim45="Good"
# We cannot start variable name with number. Thats a wrong syntax
# 1Tim="Good"
Tim_was_57="Hello"
Greeting="There" # There are two varibales "greeting" and "Greeting". Even if 
                 # both the names are same, but are different references in memory
print(Tim_was_57+' '+greeting)

age=24
print(age)

# print(greeting + age)
# TypeError: can only concatenate str (not "int") to str
"""
  The above error does not happen in case of Java i.e Programmer can concatenate any data type
  with String
"""

print(greeting +' '+ str(age))  # str() function converts Integer ref to String ref

"""
 Note :
     In Python 2.X we had below datatypes.
       (i)int
       (ii)float
       (iii)double
       (iv)long
       (v)complex
       
     But in Python 3.X, long data type support has been renoved and now int data type
     can behaves like long also
"""
a=12
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) # Output - 4.0 as "/" operator only returns floating point number
print(a//b)# Output - 4 as "//" operator returns whole number
print(a%b)

for i in range(1,8):
    print("Item = ",i)
    
for i in range(1,a//b):
    print(i)        # for i in range(1,a/b):
                    # TypeError: 'float' object cannot be interpreted as an integer
                    
                    
