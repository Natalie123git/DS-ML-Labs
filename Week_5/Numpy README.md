## **NumPy Arrays and Operations**

---

## Objective  
Array creation, manipulation, indexing, broadcasting, random generation, and linear algebra using Numpy.

---

## Tools Used  
- Python 3.x  
- NumPy  
- SciPy  

---

## Step-by-Step Process & Commands Executed  
- Imported NumPy library.
- Created a one‑dimensional array from a list.
- Created a two‑dimensional array from a nested list.
- Generated a zero‑filled array.
- Checked array attributes: shape, size, and data type.
- Performed array operations: addition, subtraction, multiplication.
- Applied aggregation functions: `sum`, `maximum`, `minimum`.
- Practiced indexing and slicing to extract rows, columns, and elements.
- Reshaped arrays into different dimensions.
- Concatenated arrays and appended new elements.
- Applied broadcasting for scalar operations across arrays.
- Generated random numbers using uniform, integer, and normal distributions.
- Selected random elements from an array.
- Performed linear algebra operations: addition, subtraction, multiplication, transpose, inverse, determinant.
- Deleted elements from arrays.
- Filtered arrays using boolean masks.
- Applied statistical functions: mean, median, mode, standard deviation.

---
## Commands Executed

### 1. Import NumPy  
Imported NumPy, the numerical computing library.  
```python
import numpy as np
```

---

### 2. Creating Arrays  
Created arrays from Python lists and generated a zero-filled array.  
```python
oneDarray = np.array([3,6,9,12,15])
oneDarray      # 1D array
twoDarray = np.array([[4,12,8],[2,6,4]]) # 2D array
twoDarray
zero_array = np.zeros((3,4))             # 3x4 zero array
zero_array
```

---

### 3. Array Attributes  
Checked shape, size, and data type of arrays.  
```python
arrayshape = twoDarray.shape
print(arrayshape)

zero_array.shape

arraysize = twoDarray.size
print(arraysize)

zero_array.size

data_type = twoDarray.dtype
print(data_type)

zero_array.dtype
```

---

### 4. Array Operations  
Performed addition, subtraction, and multiplication on arrays.  
```python
twoDarray
addarray = 2 + twoDarray
print(addarray)

subtrarray = twoDarray - 3
print(subtrarray)

multipyarray = 4 * twoDarray
print(multipyarray)
```

---

### 5. Aggregation Functions  
Calculate sum, maximum, and minimum values.  
```python
twoDarray
sum_array = twoDarray.sum()
print(sum_array)

max_val_array = twoDarray.max()
print(max_val_array)

min_val_array = twoDarray.min()
print(min_val_array)
```

---

### 6. Indexing  
Extract specific rows, columns, and slices.  
```python
twoDarray
second_array_row = twoDarray[1:,:]
print(second_array_row)

first_array_row = twoDarray[0:1,:]
print(first_array_row)

second_element_inrow = twoDarray[1:,1:]
print(second_element_inrow)

firstwo_array_infirstrow = twoDarray[0:1,0:2]
print(firstwo_array_infirstrow)

firstrow_firstindex_onwards = twoDarray[0:1,1:]
print(firstrow_firstindex_onwards)

firstrow_firstindex_onwards2 = twoDarray[0,1:]
print(firstrow_firstindex_onwards2)

firstrow_firstindex_onwards3 = twoDarray[:1,1:]
print(firstrow_firstindex_onwards3)
```

---

### 7. Array Manipulation  
Reshape arrays into different dimensions.  
```python
twoDarray
twoDarray.shape
reshaped_array = twoDarray.reshape(3,2)
print(reshaped_array)

reshaped_array2 = twoDarray.reshape(6,1)
print(reshaped_array2)
```

---

### 8. Concatenation and Append  
Combine arrays and append new elements.  
```python
oneDarray
concated_array = np.concatenate([oneDarray, oneDarray])
print(concated_array)

concated_array2 = np.concatenate([oneDarray, np.array([18,21,24])])
print(concated_array2)

appended_array = np.append(oneDarray, [18,21,24,27])
print(appended_array)

appended_array2 = np.append(twoDarray, [14,16,18])
print(appended_array2)

concated_array2D = np.concatenate([[oneDarray], np.array([[18,21,24,27,30]])])
print(concated_array2D)
```

---

### 9. Broadcasting  
Apply scalar operations across arrays.  
```python
z = np.array([5,10,15])
y = 20
print(z + y)
print(20 + z)

w = 2
print(z * w)
```

---

### 10. Random Number Generation  
Generate random arrays with different distributions.  
```python
random_num1 = np.random.rand(4,4)
print(random_num1)

random_num2 = np.random.randint(0,100,5)
print(random_num2)

random_num3 = np.random.randint(0,100,6).reshape(2,3)
print(random_num3)

random_num4 = np.random.randn(4,5)
print(random_num4)

array1 = np.array(["G","H","J","K"])
random_num5 = np.random.choice(array1,3)
print(random_num5)
```

---

### 11. Linear Algebra  
Perform matrix operations: addition, multiplication, transpose, inverse, determinant.  
```python
M = np.array([[3,5],[5,3]])
N = np.array([[7,8],[8,7]])

print(M + N)
print(M - N)
print(M * N)
print(M @ N)
multiplyres = np.matmul(M,N)
print(multiplyres)

Z = np.dot(M,N)
print(Z)

print(M / N)
print(M @ np.linalg.inv(N))

T = np.array([[7,5],[9,4]])
transposeT = np.transpose(T)
print(transposeT)

inverseM = np.linalg.inv(M)
print(inverseM)

identity_mat = np.eye(4)
print(identity_mat)

determinant = np.linalg.det(M)
print(int(determinant))
```

---

### 12. Deleting and Masking  
Remove elements and filter arrays using boolean masks.  
```python
Q = oneDarray
array_delete = np.delete(Q,3)
array_delete

R = Q != 3
new_array = Q[R]
print(new_array)
```

---

### 13. Statistical Functions  
Compute mean, median, mode, and standard deviation.  
```python
oneDarray
array_mean = np.mean(oneDarray)
array_mean

array_median = np.median(oneDarray)
print(array_median)

array4 = np.array([2,4,5,4,6,4,7,4,8,4])
from scipy import stats
array4_mode = stats.mode(array4, keepdims=False)
print(array4_mode)

array_SD = np.std(array4)
print(array_SD)
```

---

## Key Observations / Lessons Learned
- Difference between 1D vs 2D slices when indexing.  
- Reshaping arrays changes dimensions but not data.  
- Concatenation vs append for combining arrays.  
- Broadcasting simplifies scalar operations.  
- Random generation supports multiple distributions.  
- Determinant decides matrix invertibility.  
- Masking is powerful for filtering arrays.  
- Statistical functions provide quick insights into datasets.  

---
