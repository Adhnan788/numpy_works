import numpy 
import numpy as np

#np.loadtxt(file_path,delimeter=,skip_rows)

data=numpy.loadtxt("sales_data\\sales.csv",delimiter=",",skiprows=1,dtype="str")

print(data)

units_sold=data[:,3].astype("int")
print(np.sum(units_sold),"total_units_sold")

#max unit
print(np.max(units_sold),"max unit")

#min unit
print(np.min(units_sold),"min unit")

# avg unit
print(np.average(units_sold),"average unit")

#revenue
revenue=data[:,3].astype("int") * data[:,4].astype("float")
print(revenue,"revenue of each")

#total revenue
print("total revenue",np.sum(revenue))

# unit sold >8

print(data[data[:,3].astype("int")>8])

# category = electronics
print("electronics",data[data[:,2]=="Electronics"])

#flat rs100
data[:,4]=data[:,4].astype("int")-100
print("discount",data)

#north region
north_region=data[data[:,-1]=="North"]
print(north_region)
north_revenue=north_region[:,3].astype("int") * north_region[:,4].astype("float")
print(north_revenue,"revenue of north")