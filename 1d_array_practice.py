import numpy as np

# 1D Array Practice

#Extract the 3rd element
arr = np.array([3, 6, 9, 12, 15, 18])
print(arr[2])

#Extract elements from index 2 to 4
arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[2:5])

#Extract all even-indexed elements
arr = np.array([2, 4, 6, 8, 10, 12])
print(arr[::2])

#Select elements greater than 30
arr = np.array([11, 22, 33, 44, 55])
print(arr[arr > 30])

# Replace all numbers greater than 20 with -1
arr = np.array([7, 14, 21, 28, 35])
arr[arr > 20] = -1
print(arr)

#Pick elements at positions [0, 2, 4]
arr = np.array([1, 2, 3, 4, 5])
print(arr[[0, 2, 4]])

#Multiply every element by 2 using broadcasting
arr = np.array([10, 20, 30, 40])
print(arr * 2)

#Reverse the array using advanced indexing
arr = np.array([100, 200, 300, 400, 500])
print(arr[::-1])