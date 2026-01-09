import numpy as np
productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

print(productivity[productivity<8])

#working hours between 5 to 7
print(productivity[(productivity>=5) & (productivity<=7)])

# print working hrs of first employee with working hrs <8
first_employee_working_hrs=productivity[:,0]
print(first_employee_working_hrs[first_employee_working_hrs<8])

# print last two employeed working <7
last_two_employee_working_hrs=productivity[:,8:10]
print(last_two_employee_working_hrs[last_two_employee_working_hrs<7])

# <8 = 0
productivity[productivity<8]=0
print(productivity)