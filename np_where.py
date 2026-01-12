#np.where(conditions,true_value,false_value)

import numpy as np

ages=np.array([19,20,21,18,19,25])
print(np.where(ages>=20,"Adult","Teen"))
