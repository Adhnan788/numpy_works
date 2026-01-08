
import numpy as np

attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
#   

]

#functions
#sum,max,min,avg
#axis=0 // column
#axis=1 // row

#print all present count studentwise
arr=np.array(attendance)
#print(np.sum(arr,axis=1))

#print all attendace daywise
#print(np.sum(arr,axis=0))

#update student 10 attendance as present
#arr[9,1]=1
#print(arr)

#studentwise absent count
student_wise_absent_count=np.count_nonzero(arr==0,axis=1)
print(student_wise_absent_count)

day_wise_absent_count=np.count_nonzero(arr==0,axis=0)
print(day_wise_absent_count)