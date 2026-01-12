import numpy as np

# Extract the first row
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr[0])

#Extract the last column
print(arr[:, -1])

#Select elements greater than 10
arr = np.array([[2, 4, 6],
                [8, 10, 12],
                [14, 16, 18]])
print(arr[arr > 10])

#Select elements at (0,0), (1,1), (2,2)
print(arr[[0, 1, 2], [0, 1, 2]])

#Multiply every element by 5 using broadcasting
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])
print(arr * 5)

#Extract the subarray [[3,4],[7,8]]
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print(arr[0:2, 2:4])

#Multiply only the first column by 10
arr = np.array([[2, 4],
                [6, 8],
                [10, 12]])
arr[:, 0] *= 10
print(arr)