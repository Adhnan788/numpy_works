#array creation methods 
#np.array()
#np.zeros()
#np.ones()
#np.full()
#np.random.rand()

import numpy as np

zeros_array=np.zeros((2,2))
print(zeros_array)

ones_array=np.ones((3,3),dtype="int16")
print(ones_array)

full_five_array=np.full((4,4),5)
print(full_five_array)

rand_array=np.random.rand(2,4)
print(rand_array)

rand_int_array=np.random.randint(10,15,(3,3))
print(rand_int_array)