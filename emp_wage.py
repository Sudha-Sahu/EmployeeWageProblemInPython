# UC6-calculating wages till maximum hour and day is reached

import random

# Constants
WAGE_PER_HR = 20
IS_PART_TIME = 1
IS_FULL_TIME = 2
MAX_WORKING_DAY_PER_MONTH = 20
MAX_WORKING_HOUR_PER_MONTH = 100

print("Welcome to employee wage problem")

day_count = 1
total_working_hr = 0
total_wage = 0
while day_count <= MAX_WORKING_DAY_PER_MONTH or total_working_hr < MAX_WORKING_HOUR_PER_MONTH:
    is_present = random.randint(0, 2)
    if is_present == IS_PART_TIME:
        total_working_hr += 4
    elif is_present == IS_FULL_TIME:
        total_working_hr += 8
    else:
        total_working_hr += 0
    day_count += 1

total_wage = total_working_hr * WAGE_PER_HR
print("Employee total monthly wage is : ", total_wage)
