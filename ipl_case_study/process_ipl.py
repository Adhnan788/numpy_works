import numpy as np

data=np.genfromtxt("ipl_case_study\\ipl.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
print(data.shape)