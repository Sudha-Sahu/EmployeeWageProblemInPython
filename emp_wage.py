# UC1-checking employee attendance

import random

print("Welcome to employee wage problem")
emp_present = 1
attendance = random.randint(0, 1)
if attendance == emp_present:
    print("Employee is present")
else:
    print("Employee is absent")
# UC3-adding part time employee and calculating wage

import random

WAGE_PER_HR = 20
IS_PART_TIME = 1
IS_FULL_TIME = 2
working_day_hr = 0

print("Welcome to employee wage problem")

is_present = random.randint(0, 2)
if is_present == IS_PART_TIME:
    working_day_hr = 4
elif is_present == IS_FULL_TIME:
    working_day_hr = 8
else:
    working_day_hr = 0

daily_wage = working_day_hr * WAGE_PER_HR
print("Employee daily wage : ", daily_wage)
