import random

# wage and working hours are declared globaly
wage = 20
hours = 8

# function to check the attendance of an employee
def check_attendance():  
    check_attd = random.randint(0,2)
    return check_attd # if 0 than full day, 1 than half day, 2 than absent
  
# function to calculate the daily wage of an employee   
def calculate_daily_wage():
    full_day = half_day = absent = 0
    presence = check_attendance() # check_attendance method is called
    match presence:
        case 0:
            total_wage = wage * hours # daily wage of the employee is calculated
            full_day = 1
        case 1:
            total_wage = wage * (hours/2)
            half_day = 1
        case 2:
            total_wage = 0
            absent = 1
    return full_day, half_day, absent, total_wage # number of full, half and absbent days and total wage earned is returned

# function to calculate the monthly wage of an employee for 20 days
def calculate_monthly_wage():
    total_full_days = total_half_days = total_absent_days = total_monthly_wage = 0
    for i in range(20):
        # temp variable holds a tuple returned by the calculate_daily_wage method
        temp = calculate_daily_wage() # calculate_daily_wage method is called 
        total_full_days += temp[0] # no of full days is incremented 
        total_half_days += temp[1] # no of half days is incremented
        total_absent_days += temp[2] # no of absent days is incremented
        total_monthly_wage += temp[3] # total wage is incremented
       
    return total_full_days, total_half_days, total_absent_days, total_monthly_wage # returns a tuple containing total full days, half days, absent days and monthly wage

if __name__=="__main__":
    result = calculate_monthly_wage()
    print(f"\nTotal number of full days: {result[0]}\n\nTotal number of half days: {result[1]}\n\nTotal number of absent days: {result[2]}\n\nThe total wage for the month is Rs.{result[3]}/-\n")

