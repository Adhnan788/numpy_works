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

delivery_days = data[:, 6].astype('int')
late_orders = data[delivery_days > 5]
print("Orders with Delivery Days > 5" ,late_orders)

returned = data[:, 7]

returned_count = np.sum(returned == "Yes")
not_returned_count = np.sum(returned == "No")
print("Returned Orders", returned_count)
print("Non-Returned Orders", not_returned_count)

