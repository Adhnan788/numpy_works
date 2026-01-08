import numpy as np

fours_array=np.full((5,5),4)
print(fours_array)

ones_array=np.ones((3,3),dtype="int16")

ones_array[1,1]=100
print(ones_array)

fours_array[1:4,1:4]=ones_array

print(fours_array)

