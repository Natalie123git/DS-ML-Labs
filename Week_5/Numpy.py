# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:33:11 2026

@author: hp
"""

import numpy as np

#1d array from a python list
oneDarray = np.array([3,6,9,12,15])
oneDarray

#2d array from a nested python list
twoDarray = np.array([[4,12,8],[2,6,4]])
twoDarray

#zero array 
zero_array = np.zeros((3,4))
zero_array

#Array attributes

#shape

arrayshape = twoDarray.shape
print(arrayshape)

zero_array.shape

#size
arraysize = twoDarray.size
print(arraysize)

zero_array.size

#data type
data_type= twoDarray.dtype
print(data_type)

zero_array.dtype

#Array Operations

twoDarray

#addition

addarray = 2+twoDarray
print(addarray)

#subtraction
subtrarray = twoDarray-3
print(subtrarray)

#Multiplication
multipyarray = 4*twoDarray
print(multipyarray)

#Aggregation Functions

twoDarray

#sum
sum_array = twoDarray.sum()
print(sum_array)

#max
max_val_array = twoDarray.max()
print(max_val_array)

#min
min_val_array = twoDarray.min()
print(min_val_array)

#indexing
twoDarray

second_array_row = twoDarray[1:,:] #second row onwards
print(second_array_row)

first_array_row = twoDarray[0:1,:] #first row
print(first_array_row)

second_element_inrow = twoDarray[1:,1:] #second in row, second onwards
print(second_element_inrow)

firstwo_array_infirstrow = twoDarray[0:1,0:2] #first two in first row
print(firstwo_array_infirstrow)

firstrow_firstindex_onwards = twoDarray[0:1,1:]
print(firstrow_firstindex_onwards) #gives a 2D array

firstrow_firstindex_onwards2 = twoDarray[0,1:]
print(firstrow_firstindex_onwards2) #gives a 1D array

firstrow_firstindex_onwards3 = twoDarray[:1,1:]
print(firstrow_firstindex_onwards3) #gives a 2D array

# Array Manipulation
twoDarray

twoDarray.shape
reshaped_array = twoDarray.reshape(3,2)
print(reshaped_array)

reshaped_array2 = twoDarray.reshape(6,1)
print(reshaped_array2)

#Concantenate Arrays
oneDarray
concated_array = np.concatenate([oneDarray,oneDarray])
print(concated_array)

concated_array2 = np.concatenate([oneDarray,np.array([18,21,24])])
print(concated_array2)

#append
appended_array = np.append(oneDarray,[18,21,24,27])
print(appended_array)

appended_array2 = np.append(twoDarray,[14,16,18])
print(appended_array2)

#append to 2D: both should be 2d
concated_array2D = np.concatenate([[oneDarray],np.array([[18,21,24,27,30]])])
print(concated_array2D)

#broadcasting
z= np.array([5,10,15])
y=20
print(z+y)
print(20+z)

w=2
print(z*w)

#Random Number Generation

random_num1 = np.random.rand(4,4)
print(random_num1)

random_num2 = np.random.randint(0,100,5)
print(random_num2)

random_num3 = np.random.randint(0,100,6).reshape(2,3)
print(random_num3)

#random for normal distribution numbers
random_num4 = np.random.randn(4,5)
print(random_num4)

#can use choice() to choose any random varibles from an array

array1 = np.array(["G","H","J","K"])
array1
random_num5 = np.random.choice(array1,3)
print(random_num5)

#Linear Algebra
#Matrix Addition

M = np.array([[3,5],[5,3]])
N = np.array([[7,8],[8,7]])
M,N
print(M + N)

#Matrix Subtraction
print(M - N)

#Matrix Multipilication
print(M*N) #* only does element wise  multiplication and (Column-wise)

print(M@N) #proper matrix multiplication

#OR
multiplyres = np.matmul(M,N)
print(multiplyres)

#Normal Matrix Multiplication
Z = np.dot(M,N)
print(Z)

#Matrix division
print(M/N)

#Normal matrix multiplication
M @ np.linalg.inv(N)

#Transposing a matrix
T = np.array([[7,5],[9,4]])
transposeT = np.transpose(T)
print(transposeT)

#Inversing a matrix: indentity matrix divided by the original
#it must be a square, 2x2,3x3 etc
inverseM = np.linalg.inv(M)
print(inverseM)

#identity Matrix:1 in diagonal
identity_mat = np.eye(4)
print(identity_mat)

#determinant of a matrix
#- If the determinant = 0 → the matrix is singular (no inverse exists).
#- If the determinant ≠ 0 → the matrix is invertible.

determinant = np.linalg.det(M)
print(int(determinant))

#Delete elements in an array
Q= oneDarray
array_delete = np.delete(Q,3)
array_delete

R= Q !=3
new_array = Q[R]
print(new_array)

#Statistical Functions

oneDarray

#mean
array_mean = np.mean(oneDarray)
array_mean

#median
array_median = np.median(oneDarray)
print(array_median)

#Mode: numpy does not have the mode method, so we use scipy can be used
array4 = np.array([2,4,5,4,6,4,7,4,8,4])
from scipy import stats
array4_mode = stats.mode(array4,keepdims=False) #keeps the dimension if True that is th format of your array
print(array4_mode)

#standard deviation
array_SD = np.std(array4)
print(array_SD)
