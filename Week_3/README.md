# Arithmentic, Python Operators and Strings

## Objective
This week focused on arithmetic, comparison, logical, assignment, bitwise, membership, identity operators, and string manipulation.

---

## Tools Used
- Python   
- Spyder IDE  
- GitHub for documentation 

---

## Step‑by‑Step Process

1. Declared integer variables and performed **addition, subtraction, multiplication, division, floor division, modulo, and exponentiation**.  
2. Applied **comparison operators** (`>`, `<`, `==`, `!=`, `>=`, `<=`) to evaluate conditions.  
3. Practiced **logical operators** (`and`, `or`, `not`) to combine or negate conditions.  
4. Used **assignment operators** (`+=`, `-=`, `*=`, `/=`, `//=`, `**=`) to reassign values dynamically.  
5. Explored **bitwise operators** (`&`, `|`, `^`, `~`, `<<`, `>>`) to manipulate integers at the binary level.  
6. Checked **membership operators** (`in`, `not in`) to verify elements within lists.  
7. Compared objects with **identity operators** (`is`, `is not`) to test storage references.  
8. Manipulated **strings** with methods like `upper()`, `lower()`, `isalpha()`, `isdigit()`, `isupper()`, `islower()`.  
9. Practiced **splitting and joining strings** using `split()` and `join()`.  
10. Replaced substrings with `replace()` to modify text dynamically.  
11. Verified prefixes and suffixes with `startswith()` and `endswith()`.  

---

## Commands Executed

1. **Arithmetic Operators**  
   - Addition, subtraction, multiplication, division, floor division, modulo, exponentiation.  
   ```python
   j = 65
   k = 7
   print(j + k)   # Addition
   j - k          # Subtraction
   j * k          # Multiplication
   j / k          # Division
   j // k         # Floor division
   j % k          # Modulo
   j ** k         # Exponential
   ```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Arithmetic_Operators.png)

2. **Comparison Operators**  
   - Greater than, less than, equal to, not equal to, etc.  
   ```python
   j > k
   j < k
   j == k
   j >= k
   j <= k
   j != k
   ```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Comparison_Operators.png)

3. **Logical Operators**  
   - `and`, `or`, `not`.  
   ```python
   j > 57 and k < 78
   j < 57 and k < 78
   j < 57 or k < 78
   j < 57 or k > 78

   
   not(j > 57)
   not(j < 57)
   ```

### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Logical_Operators.png)

4. **Assignment Operators**  
   - Reassign values with `+=`, `-=`, `*=`, `/=`, `//=`, `**=`.  
   ```python
   j += 20
   j -= 20
   j *= 3
   j /= 3
   j //= 4
   j **= 3
   ```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Assignment_Operators.png)

5. **Bitwise Operators**  
   - Operate at the binary level (`&`, `|`, `^`, `~`, `<<`, `>>`).  
   ```python
   p = 25
   q = 44
   bin(p)
   bin(q)
   p & q
   p | q
   p ^ q
   ~p
   p >> 1
   p >> 2
   p >> 3
   p << 1
   p << 2
   ```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Bitwise_Operators.png)

6. **Membership Operators**  
   - Check if an element is in a list.  
   ```python
   letters = ["f","h","r","y","s"]
   "h" in letters
   "b" in letters
   "b" not in letters
   "h" not in letters
   ```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Membership_Operators.png)

7. **Identity Operators**  
   - Compare object identities.  
   ```python
   d = [5,10,15,20,25]
   e = [5,10,15,20,25]
   d is e
   d is not e
   ```
### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Identity_Operators.png)

8. **Strings**  
   - Case conversion, checks (`isalpha`, `isdigit`, `isupper`, `islower`), splitting, joining, replacing, startswith/endswith.  
   ```python
   Lesson = "ParoCyber VBS"
   Lesson.upper()
   Lesson.lower()
   Lesson.isalpha()
   Lesson.isdigit()
   Lesson.isupper()
   Lesson.islower()

   Running = "I hate running"
   Split = Running.split(" ")
   "_".join(Running.split(" "))
   Running = "I hate running"
   Running.replace("running", "treadmills")

   Sports = "marathon"
   Sports.startswith("m")
   Sports.startswith("r")
   Sports.endswith("n")
   Sports.endswith("h")
   ```

### Screenshots of Results
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Strings1.png)
![Result1](https://github.com/Natalie123git/DS-ML-Labs/blob/main/Week_3/Week_3_Results_Strings2.png)

---

## Key Observations and Lessons Learned
- Arithmetic, comparison, logical, and assignment operators form the foundation of Python programming.  
- Bitwise operators allow manipulation at the binary level, useful for low‑level tasks.  
- Membership and identity operators enable us to detect the components of sets.  
- String methods (`upper`, `lower`, `split`, `join`, `replace`) provide powerful text manipulation tools.  

---
