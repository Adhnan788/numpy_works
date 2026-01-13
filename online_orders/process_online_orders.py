import numpy 
import numpy as np

#np.loadtxt(file_path,delimeter=,skip_rows)

data=numpy.loadtxt("online_orders\\online_orders.csv",delimiter=",",skiprows=1,dtype="str")

print(data)
print("Shape of dataset:", data.shape)

total_orders = data.shape[0]
print(total_orders)

unit_price = data[:, 4].astype(int)
avg_unit_price = np.mean(unit_price)
print("Average Unit Price:", avg_unit_price)



