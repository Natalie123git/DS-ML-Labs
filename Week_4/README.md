# String formatting, control flow, loops, functions, and built‑in modules

## Objective
The goal of this lab is to reinforce practical Python programming skills, in string formatting, functions and modules.

---

## Tools Used
- Python 
- IDE: Spyder
- GitHub for documentation  
- Markdown for README formatting  

---

## Step‑by‑Step Process

1. Practiced **string formatting** using concatenation, f‑strings, and the `.format()` method to combine text and variables seamlessly.  
2. Applied **control flow** with `if`, `if‑else`, nested `if`, and `if‑elif‑else` statements to evaluate conditions and execute code blocks accordingly.  
3. Used **logical operators** (`and`, `or`) and **ternary operators** to express concise conditional logic.  
4. Implemented **for loops** to iterate over lists, dictionaries, and sequences, including tasks like summing values and filtering odd numbers.  
5. Applied **while loops** to repeat processes until conditions were met, including summing values and iterating through lists and dictionaries.  
6. Defined **functions** (`add`, `subt`, `greet`, `sumandproduct`) to organize reusable code, return values, and improve readability.  
7. Practiced **lambda functions** for quick, inline operations such as addition and sorting dictionaries by values.  
8. Explored **built‑in functions**:
  - `map()` to transform lists (e.g., squaring numbers, capitalizing strings).  
  - `filter()` to select items based on conditions (e.g., even numbers, positive numbers).  
  - `reduce()` to cumulatively combine elements (e.g., product of numbers, maximum value).  
  - `sum()`, `max()`, and `min()` to aggregate values efficiently.  
9. Documented **observations** on readability: f‑strings are most concise, `map` and `filter` simplify transformations, and `reduce` is powerful for cumulative tasks.  

---
##Commands Executed
---

### 1. String Formatting
- Concatenation with `+` and `str()`
- F‑strings for concise formatting
- `.format()` method with positional and named placeholders

```python
name = "Natalie"
age = 99
print("Hello, my name is "+ name +" and I am " +str(age) + " years old.")

food = "rice and tofu"
print("I love " + food)

print(f"Hello, my name is {name} and I am {age} years old.")
print(f"I love {food}")

print("Hello, my name is {} and I am {} years old.".format(name,age))
print("Hello, my name is {0} and I am {1} years old.".format(name,age))
print("Hello, my name is {name1} and I am {age1} years old.".format(name1 = name,age1 = age))
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_4/Week_4_Results_String_formatting.png)
---

### 2. Control Flow
- Simple `if` conditions
- `if-else` for branching
- Nested `if` for multiple levels
- `if-elif-else` for sequential conditions
- Ternary operators for concise conditional expressions

```python
k = 16
if k>0 and k % 2 == 0:
    print("k is an even number")

j = 15
if j<0 or j % 2 == 1:
    print("j is an odd number")

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

age=99
if age >=100:
    if age >150:
        print("You are full of wisdom and need to share it.")
    else:
        print("You have some wisdom but need to add a few more years to be full of wisdom.")
else:
    print("You have no wisdom at all.")

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

number = 12
result = "Positive" if number > 0 else "Negative"
print(result)

number2 = 17
result2 = "Even" if number2 % 2 == 0 else "Odd"
print(result2)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_4/Week_4_Results_Control_Flow1.png)
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_4/Week_4_Results_Control_Flow2.png)
---

### 3. Loops
- For loops: iterate over lists, dictionaries, and sequences
- While loops: repeat until condition is false
- Summation examples with both loop types

```python
sports = ["tennis", "volleyball", "soccer", "basketball"]
for sport in sports:
    print(sport)

list1 = [5,10,15,20,25,30,35,40,45,50]
for i in list1:
    if i%2==1:
        print(i)

person = {"name":"Natalie","age":99,"city":"Barcelona"}
for key,value in person.items():
    print(f"{key}:{value}")

tens = [10,20,30,40,50,60]
total = 0
for value in tens:
    total += value
print(total)

m = 1
while m <=5:
    print(m)
    m+=1

floral = ["Rose", "Sunflower", "lily", "Daisy"]
a=0
while a <=2:
    print(floral[a])
    a +=1

mydict = {"name":"Natalie","age":99,"city":"Barcelona"}
keys = list(mydict.keys())
index = 0
while index < len(keys):
    key = keys[index]
    value = mydict[key]
    print(key,value)
    index+=1

Sevens = [7,14,21,28,35]
total1 = 0
index1 = 0
while index1 < len(Sevens):
    total1+=Sevens[index1]
    index1+=1
print("Sum of numbers:",total1)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_4/Week_4_Results_Loops.png)
---

### 4. Functions & Modules
- Defining reusable functions (`add`, `subt`, `greet`)
- Returning multiple values (sum and product)
- Lambda functions for quick one‑liners
- Sorting with `lambda` keys

```python
def add(y,z):
    d=y+z
    return d
add(55,45)

def subt(b,c):
    e=b-c
    return e
subt(75,73)

def greet(name):
    return f"Hola, {name}!"
greeting = greet("Natalie")
print(greeting)

def sumandproduct(i,o):
    return i+o,i*o
result3=sumandproduct(5, 7)
print("Sum:",result3[0])
print("Product:",result3[1])

add1 = lambda p,q:p+q
print(add1(55,45))

students = [{"name":"Natalie","score":87},{"name":"June","score":86}]
sorted_students=sorted(students,key=lambda s:s["score"])
print(sorted_students)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_4/Week_4_Results_Functions_and_Modules.png)
---

### 5. Built‑in Functions
- `map()` for transformations
- `filter()` for selecting items
- `reduce()` for cumulative operations
- `sum()`, `max()`, `min()` for aggregation

```python
numbers3 = [2,4,6,8,10]
squared = map(lambda r:r**2,numbers3)
print(list(squared))

cities = ["lagos", "accra", "pretoria", "barcelona"]
capcities = map(lambda t:t.capitalize(),cities)
print(list(capcities))

nines = [9,18,27,36,45]
evens = filter(lambda u:u%2==0,nines)
print(list(evens))

numbers4 = [-5,-7,6,8,-15,-71]
pos_num = filter(lambda v:v>=0,numbers4)
print(list(pos_num))

from functools import reduce
numbers5 = [2,4,6,8,10]
product = reduce(lambda w,x:w*x,numbers5)
print(product)

eights = [8,40,24,32,16]
maxnum = reduce(lambda w,x:w if w>x else x, eights)
print(maxnum)

fours = [4,8,12,16,20]
total = sum(fours)
print(total)

threes = [3,6,9,12,15]
maxnum1 = max(threes)
print(maxnum1)

cars = ["honda","benz","BMW","Toyota"]
longest_word = max(cars, key=len)
print(longest_word)

sixes = [6,12,18,24,30]
min_num = min(sixes)
print(min_num)

marks = {"Natalie":99, "Thomas":98,"George":97}
min_mark = min(marks.values())
print(min_mark)
```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_4/Week_4_Results_Built%E2%80%91in_Functions.png)
---

## Key Observations / Lessons Learned
- F‑strings are the most concise and readable way to format strings.  
- Control flow allows branching logic and concise decision‑making with ternary operators.  
- Loops are powerful for iterating over collections and performing cumulative tasks.  
- Functions improve reusability and readability; lambdas are useful for quick operations.  
- Built‑in functions (`map`, `filter`, `reduce`, `sum`, `max`, `min`) simplify common tasks.  
- Professional documentation requires clear structure, code snippets, and screenshots.

---
