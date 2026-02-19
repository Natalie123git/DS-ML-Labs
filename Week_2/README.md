# Lab Title: Working with Lists, Tupples and Dictionaries

## Objective
To practice Python’s core data structures — **lists, tuples, and dictionaries** — and understand their properties, mutability, and common operations.

## Tools Used
- Python 
- Sypder  


## Lab 1: Lists and Their Mutability

### Step‑by‑Step Process
1. Created a list of colours.  
2. Appended new items.  
3. Extended the list with multiple items.  
4. Inserted an item at a specific position.  
5. Removed and popped items.  
6. Indexed to find positions.  
7. Counted occurrences.  
8. Sorted and reversed the list.

### Commands Executed
```python
colours = ["red","green","yellow","blue","purple","orange"]
colours.append("burgundy")
colours.extend(["brown","black","white"])
colours.insert(1,"pink")
colours.remove("yellow")
pop_variable = colours.pop(5)
print(pop_variable)
myindex = colours.index("brown")
mycount = colours.count("blue")
colours.sort()
colours.reverse()
```
### Screenshots of results
#### Appending and extending
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_2/Week_2_Results%201of6.png)
#### Inserting and removing
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_2/Week_2_Results%202of6.png)
#### Popping, indexing and counting
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_2/Week_2_Results%203of6.png)
#### Sorting and reversing
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_2/Week_2_Results%204of6.png)

### Key Observations / Lessons Learned
- Lists are **mutable** (can be changed after creation).  
- Useful for ordered collections where frequent updates are needed.  
- Methods like `append`, `extend`, and `insert` add flexibility.  
- Sorting and reversing allow quick reorganization of data.  

---

## Lab 2: Tuples (Immutable)

### Step‑by‑Step Process
1. Created a tuple of animals.  
2. Counted occurrences of an element.  
3. Found the index of an element.  
4. Accessed elements by position.  

### Commands Executed
```python
animals = ("dog","cat","cow","cat")
animals.count("cat")
animals.index("cow")
print(animals[2])
```
### Screenshots of results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_2/Week_2_Results%205of6.png)

### Key Observations / Lessons Learned
- Tuples are **immutable** (cannot be changed after creation).  
- Still allow counting and indexing operations.  
- Best used for fixed collections of data.  

---

## Lab 3: Dictionaries (Key‑Value Pairs)

### Step‑by‑Step Process
1. Created dictionaries using different methods.  
2. Extracted values with '.get()'.  
3. Retrieved items, keys, and values.  
4. Updated dictionary with new key‑value pairs.  

### Commands Executed
```python
mydictionary = dict(Name="Thomas", Age=108, City="Lagos")
mydictionary = dict([("Name","Thomas"),("Age",108),("City","Lagos")])
mydictionary = {"Name":"Thomas","Age":108,"City":"Lagos"}

age = mydictionary.get("Age")
myitems = mydictionary.items()
mykeys = mydictionary.keys()
myvalues = mydictionary.values()
mydictionary.update({"gender":"Male"})
```
### Screenshots of results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_2/Week_2_Results%205of6.png)

### Key Observations / Lessons Learned
- Dictionaries store **unordered key‑value pairs**.  
- Multiple ways to create them.  
- `.get()`, `.items()`, `.keys()`, `.values()` are powerful for data extraction.  
- Updating is straightforward with `.update()`.  

---

## Overall Reflection
- Lists taught mutability and dynamic data handling.  
- Tuples reinforced immutability and stability.  
- Dictionaries introduced flexible key‑value storage.  
- These structures form the backbone of Python programming and are essential for data science workflows.  

---
