# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:47:18 2026

@author: hp
"""

##String Formatting
#For creating readable and well-structured output in Python programming
#can combine text and variables seamlessly.
#it should always be strings, even numbers

name = "Natalie"
age = 99
print("Hello, my name is "+ name +" and I am " +str(age) + " years old.")

food = "rice and tofu"
print("I love " + food)

#F_strings provide a more consice and readable way to format strings by embedding expressions directly
#no need for str(), shows that everything is strings
print(f"Hello, my name is {name} and I am {age} years old.")
print(f"I love {food}")

#dot format using placeholders in various formats
print("Hello, my name is {} and I am {} years old.".format(name,age))
#OR
print("Hello, my name is {0} and I am {1} years old.".format(name,age))
#OR
print("Hello, my name is {name1} and I am {age1} years old.".format(name1 = name,age1 = age))

#Control Flow: If Statements

#if statements
k = 16
if k>0 and k % 2 == 0:
    print("k is an even number")
    
j = 15
if j<0 or j % 2 == 1:
    print("j is an odd number")


#if-else
h = int(input("Enter a number: "))
if h>0 and h % 2 == 0:
    print("h is an even number")
else:
    print("h is an odd number")
    
l = 19
if l > 0 and l % 2 == 0:
    print ("l is an even number")
else:
    print("l is either a negative number and/or an odd number")

#Nested if
age=99
if age >=100:
    if age >150:
        print("You are full of wisdom and need to share it.")
    else:
        print("You have some wisdom but need to add a few more years to be full of wisdom.")
else:
    print("You have no wisdom at all.")


#If-Elif-Else Statements: to test multiple conditions sequentially and execute the corresponding code block of the first true condition
age=99
if age>=100 and age <150:
    print("You have adequate wisdom")
elif age>= 100 and age>150:
    print("You have plenty of wisdom")
else:
    print("You have no wisdom.")
    
score = int(input("Enter a score: "))
if score >= 95:
    print("A+")
elif score >=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("fail")

#Tenary Operators: a concise way to express conditional statements.
number = 12
result = "Positive" if number > 0 else "Negative"
print(result)

number2 = 17
result2 = "Even" if number2 % 2 == 0 else "Odd"
print(result2)

#LOOPS

#For loops: used to iterate over a sequence e.g a list, tuple, or string and execute a block of code for each element in the sequence.
#know number of times you are going to iterate/repeat a process

#iterating over a list
sports = ["tennis", "volleyball", "soccer", "basketball"]
for sport in sports:
    print(sport)

#iterating over a list to print odd numbers
list1 = [5,10,15,20,25,30,35,40,45,50]
for i in list1:
    if i%2==1:
        print(i)

#iterating over a dictionary
person = {"name":"Natalie","age":99,"city":"Barcelona"}
for key,value in person.items():
    print(f"{key}:{value}")

#iterating to get sum
tens = [10,20,30,40,50,60]
total = 0
for value in tens:
    total += value
print(total)

#While loop:as long as the condition is true repeat yourself
#Looping and printing a value
#Don't forget the break otherwise you will go into an infinity loop
m = 1
while m <=5:
    print(m)
    m+=1
    
#looping over a list and printing the items in the list
floral = ["Rose", "Sunflower", "lily", "Daisy"]
a=0
while a <=2:
    print(floral[a])
    a +=1

#Looping over a dictionary and printing each key-value pair
mydict = {"name":"Natalie","age":99,"city":"Barcelona"}
keys = list(mydict.keys()) # Convert dictionary keys to list for indexing
index = 0
while index < len(keys):
    key = keys[index]
    value = mydict[key]
    print(key,value)
    index+=1
    
#Calculating the sum of numbers in a list using a while loop
Sevens = [7,14,21,28,35]
total1 = 0
index1 = 0
while index1 < len(Sevens):
    total1+=Sevens[index1]
    index1+=1
print("Sum of numbers:",total1)

#Functions and modules
#Functions are blocks of reusable code that perform a specific task. They help in organizing code, promoting reusability, and improving readability.
#it comes with definition, block of code, function name

def add(y,z):
    #This code adds two numbers
    
    d=y+z
    return d

add(55,45)

def subt(b,c):
    e=b-c
    return e

subt(75,73)

#function to greet user
def greet(name):
    #Greets the user
    return f"Hola, {name}!"

#Calling the function
greeting = greet("Natalie")
print(greeting)

#Function to return the sum and product of two numbers
def sumandproduct(i,o):
    #adds and multiplies the numbers
    return i+o,i*o

result3=sumandproduct(5, 7)
print("Sum:",result3[0])
print("Product:",result3[1])


#lambda function: no defining it, need a quick result
#lambda, the parameters and then the expression
#Its basically saying for these/this value do this
add1 = lambda p,q:p+q
print(add1(55,45))

students = [{"name":"Natalie","score":87},{"name":"June","score":86}]
sorted_students=sorted(students,key=lambda s:s["score"])
print(sorted_students) #add reverse true for descending

#Built in Functions: perform common operations efficiently in Python.

#e.g 1 map(fuction, iterable): Applies the given function to each item in the iterable and returns a new iterable with the results.

# #Finding the square of the numbers in the list
numbers3 = [2,4,6,8,10]
squared = map(lambda r:r**2,numbers3)
print(list(squared))

#Capitalizing the first letter of each word in a list of strings using map:
cities = ["lagos", "accra", "pretoria", "barcelona"]
capcities = map(lambda t:t.capitalize(),cities)
print(list(capcities))

#e.g 2 filter(function,iterable):Filters elements from an iterable based on the given function's truthiness.

#Finding the even numbers in the list
nines = [9,18,27,36,45]
evens = filter(lambda u:u%2==0,nines)
print(list(evens))

#Filtering out negative numbers from a list:
numbers4 = [-5,-7,6,8,-15,-71]
pos_num = filter(lambda v:v>=0,numbers4)
print(list(pos_num))

# e.g 3 reduce(function, iterable[, initializer]):
#Applies the given function cumulatively to the items of the iterable, from left to right, to reduce the iterable to a single value.

#Finding the product of the elements in the list
from functools import reduce
numbers5 = [2,4,6,8,10]
product = reduce(lambda w,x:w*x,numbers5)
print(product)

#Finding the maximum element in a list using reduce:
eights = [8,40,24,32,16]
maxnum = reduce(lambda w,x:w if w>x else x, eights)
print(maxnum)

# e.g 4 sum(iterable[, start]): Returns the sum of all elements in the iterable.

#find the sum of the numbers in the list
fours = [4,8,12,16,20]
total = sum(fours)
print(total)

# e.g 5 max(iterable[, key, default]):Returns the maximum element from the iterable.

#Finding the maximum value in a list
threes = [3,6,9,12,15]
maxnum1 = max(threes)
print(maxnum1)

#Finding the longest string in a list:
cars = ["honda","benz","BMW","Toyota"]
longest_word = max(cars, key=len)
print(longest_word)

# e.g 6 min(iterable[, key, default]):Returns the minimum element from the iterable.
sixes = [6,12,18,24,30]
min_num = min(sixes)
print(min_num)

#Finding the minimum value in a dictionary:
marks = {"Natalie":99, "Thomas":98,"George":97}
min_mark = min(marks.values())
print(min_mark)