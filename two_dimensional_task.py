import numpy as np

array=np.array([
    [43,42,45,34,23],
    [23,45,45,34,37],
    [37,38,39,40,45]
])

#display marks of hari
print(array[1])

#display maths mark of hari
print(array[1,0])

#display malayalam marks of all students
print(array[:,2])

#display malayalam and cs marks of all students
print(array[:,2:4])

#display english and malayalam marks of hari and cibin
print(array[1:3,1:3])