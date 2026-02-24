# Week 3 Labs: Arithmentic, Python Operators and Strings

## Objective
This week focused on arithmetic, comparison, logical, assignment, bitwise, membership, identity operators, and string manipulation.

---

## Tools Used
- Python   
- Spyder IDE  
- GitHub for documentation 

---

## Step‑by‑Step Process
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

3. **Logical Operators**  
   - `and`, `or`, `not`.  
   ```python
   j > 57 and k < 78
   j < 57 or k < 78
   not(j > 57)
   ```

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

5. **Bitwise Operators**  
   - Operate at the binary level (`&`, `|`, `^`, `~`, `<<`, `>>`).  
   ```python
   p = 25
   q = 44
   bin(p), bin(q)
   p & q
   p | q
   p ^ q
   ~p
   p >> 1
   p << 2
   ```

6. **Membership Operators**  
   - Check if an element is in a list.  
   ```python
   letters = ["f","h","r","y","s"]
   "h" in letters
   "b" not in letters
   ```

7. **Identity Operators**  
   - Compare object identities.  
   ```python
   d = [5,10,15,20,25]
   e = [5,10,15,20,25]
   d is e
   d is not e
   ```

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
   Running.split(" ")
   "_".join(Running.split(" "))
   Running.replace("running", "treadmills")

   Sports = "marathon"
   Sports.startswith("m")
   Sports.endswith("n")
   ```

---

## Screenshots of Results


---

## Key Observations / Lessons Learned
- Arithmetic, comparison, logical, and assignment operators form the foundation of Python programming.  
- Bitwise operators allow manipulation at the binary level, useful for low‑level tasks.  
- Membership and identity operators highlight differences between values and object references.  
- String methods (`upper`, `lower`, `split`, `join`, `replace`) provide powerful text manipulation tools.  
- Professional documentation in Markdown makes labs reproducible and clear.  

---
