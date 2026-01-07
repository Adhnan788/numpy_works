import numpy as np

array=np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]
])

print(array.ndim)
print(array.size)
print(array.shape)

#fetch 0th row

print(array[0])
print(array[2])

#syntax arr[row,col]
#slicing rows
#fetching rows from 1 to 2
print(array[1:3])

#fetching rows from 0 to 1
print(array[0:2])

# column slice
print(array[:,1:3])
print(array[:,0:2])

print(array[:,1])

print(array[::2])

print(array[2,1])

print(array[1:3,1:3])