# Week 4 Labs – String formatting, control flow, loops, functions, and built‑in modules

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
- Used **logical operators** (`and`, `or`) and **ternary operators** to express concise conditional logic.  
- Implemented **for loops** to iterate over lists, dictionaries, and sequences, including tasks like summing values and filtering odd numbers.  
- Applied **while loops** to repeat processes until conditions were met, including summing values and iterating through lists and dictionaries.  
- Defined **functions** (`add`, `subt`, `greet`, `sumandproduct`) to organize reusable code, return values, and improve readability.  
- Practiced **lambda functions** for quick, inline operations such as addition and sorting dictionaries by values.  
- Explored **built‑in functions**:
  - `map()` to transform lists (e.g., squaring numbers, capitalizing strings).  
  - `filter()` to select items based on conditions (e.g., even numbers, positive numbers).  
  - `reduce()` to cumulatively combine elements (e.g., product of numbers, maximum value).  
  - `sum()`, `max()`, and `min()` to aggregate values efficiently.  
- Documented **observations** on readability: f‑strings are most concise, `map` and `filter` simplify transformations, and `reduce` is powerful for cumulative tasks.  

---

### 1. String Formatting
- Concatenation with `+` and `str()`  
- F‑strings for concise formatting  
- `.format()` method with positional and named placeholders  

```python
name = "Natalie"
age = 99
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")
print(f"Hello, my name is {name} and I am {age} years old.")
print("Hello, my name is {} and I am {} years old.".format(name, age))
```
### Screenshots of Results
![Result1]()
---

### 2. Control Flow (If Statements)
- Simple `if` conditions  
- `if-else` for branching  
- Nested `if` for multiple levels  
- `if-elif-else` for sequential conditions  
- Ternary operators for concise conditional expressions  

```python
k = 16
if k > 0 and k % 2 == 0:
    print("k is an even number")

number = 12
result = "Positive" if number > 0 else "Negative"
print(result)
```

---

### 3. Loops
- **For loops**: iterate over lists, dictionaries, and sequences  
- **While loops**: repeat until condition is false  
- Summation examples with both loop types  

```python
sports = ["tennis", "volleyball", "soccer", "basketball"]
for sport in sports:
    print(sport)

m = 1
while m <= 5:
    print(m)
    m += 1
```

---

### 4. Functions and Modules
- Defining reusable functions (`add`, `subt`, `greet`)  
- Returning multiple values (sum and product)  
- Lambda functions for quick one‑liners  
- Sorting with `lambda` keys  

```python
def greet(name):
    return f"Hola, {name}!"

greeting = greet("Natalie")
print(greeting)

add1 = lambda p, q: p + q
print(add1(55, 45))
```

---

### 5. Built‑in Functions
- `map()` for transformations  
- `filter()` for selecting items  
- `reduce()` for cumulative operations  
- `sum()`, `max()`, `min()` for aggregation  

```python
from functools import reduce

numbers = [2, 4, 6, 8, 10]
squared = map(lambda r: r**2, numbers)
print(list(squared))

evens = filter(lambda u: u % 2 == 0, [9, 18, 27, 36, 45])
print(list(evens))

product = reduce(lambda w, x: w * x, numbers)
print(product)
```

---

## 📸 Screenshots of Results

---

## 🔑 Key Observations / Lessons Learned
- F‑strings are the most concise and readable way to format strings.  
- Control flow allows branching logic and concise decision‑making with ternary operators.  
- Loops are powerful for iterating over collections and performing cumulative tasks.  
- Functions improve reusability and readability; lambdas are useful for quick operations.  
- Built‑in functions (`map`, `filter`, `reduce`, `sum`, `max`, `min`) simplify common tasks.  
- Professional documentation requires clear structure, code snippets, and screenshots.

---
