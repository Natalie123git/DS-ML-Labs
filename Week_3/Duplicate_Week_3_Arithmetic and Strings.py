# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:07:19 2026

@author: hp
"""

#Addition
j=65
k=7
print(j+k)

#Subtraction
j-k

#Multiplication
j*k

#Division
j/k

#floor division: returns the whole number and ignores the remainder
j//k

#Modulo: Returns the remainder only
j%k

#Exponential
j**k

#Comparison Operators: returns boolean answer
j>k
j<k
j==k
j>=k
j<=k
j!=k  #not equal to

#Logical Operators: (and AND or) Returns boolean answers
j>57 and k<78
j<57 and k<78
j<57 or k<78
j<57 or k>78

#not: is a negation, returns the opposite of the correct answer
not(j>57)
not(j<57)

#Assignment operator:changes the value by reassigning it to the answer
j+=20
j
j-=20
j
j*=3
j
j/=3
j
j//=4
j
j**=3
j

#Bitwise Operations: References intergers in binary levels (0s and 1s)
#&|^~<<>>
# Bitwise Operators Reference
# | Symbol | Operator Name        | Typographic Name   | Action                                | 4-bit Example (x=1010, y=1100) |
# |--------|----------------------|-------------------|---------------------------------------|--------------------------------|
# | &      | Bitwise AND          | Ampersand         | Sets bit to 1 if both bits are 1      | 1010 & 1100 = 1000             |
# | |      | Bitwise OR           | Pipe / Vertical Bar | Sets bit to 1 if either bit is 1     | 1010 | 1100 = 1110            |
# | ^      | Bitwise XOR          | Caret             | Sets bit to 1 if bits are different   | 1010 ^ 1100 = 0110             |
# | ~      | Bitwise NOT          | Tilde             | Flips each bit (0 → 1, 1 → 0)         | ~1010 = 0101 then add 1        |
# | <<     | Left Shift           | Double Less-Than  | Shifts bits left, filling with 0s     | 1010 << 1 = 0100               |
# | >>     | Right Shift          | Double Greater-Than | Shifts bits right, filling with 0s   | 1010 >> 1 = 0101              |

p=25
q=44
bin(p) #if you want to know the binary forms of the numbers
bin(q)
p&q
p|q
p^q
~p #~ acts as the not/negation or a variable
p>>1 #shifting the binary figure to the right, basically dividing the number by 2 over and over again with each shift
p>>2
p>>3
p<<1 #shifting the binary form to the left, which is the same as basically multiplying it by 2 over and over again with each shift
p<<2

#Membership Operators: "in" and "not in"
#These check whether a variable is a member of the set or not
letters = ["f","h","r","y","s"]
print("h" in letters)
print("b" in letters)
print("b" not in letters)
print("h" not in letters)

#Identity Operators: "is" and "is not"
#if this is that, this looks at the storage positon
d = [5,10,15,20,25]
e = [5,10,15,20,25]
print(d is e)
print(d is not e)

#STRINGS
Lesson = "ParoCyber VBS"
Lesson

#Modify by changing everything to uppercase or lowercase using upper() and lower()
Lesson = Lesson.upper()
Lesson
Lesson = Lesson.lower()
Lesson

#Check whether everything is in alphabets using isalpha()
Isitinalpha = Lesson.isalpha()
Isitinalpha

#Check whether everything is in numbers format using isdigit()
Isitindigits = Lesson.isdigit()
Isitindigits

#Check whether everything is in uppercase using isupper()
IsitinUcase = Lesson.isupper()
IsitinUcase

#Check whether everything is in lowercase using islower()
IsitinLcase = Lesson.islower()
IsitinLcase

#Spliting and joining strings using split() and join()
Running = "I hate running"
Split = Running.split(" ")
Split
print("_".join(Split))

#Replacing variables using replace()
Running = "I hate running"
Running = Running.replace("running", "treadmills")
Running

#using "startswith()" to see what a string starts with and "endswith()" to see what a string ends with
Sports = "marathon"
Sports.startswith("m")
Sports.startswith("r")
Sports.endswith("n")
Sports.endswith("h")
