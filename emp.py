import random

wage = 20
hours = 8

# function to check the attendance of an employee
def check_attendance():  
    check_attd = random.randint(0,2)
    return check_attd

# function to calculate the daily wage of an employee   
def calculate_daily_wage():
    full_day = half_day = absent = total_hours= 0
    presence = check_attendance()
    match presence:
        case 0:
            total_wage = wage * hours
            full_day = 1
            total_hours = hours
        case 1:
            total_wage = wage * (hours/2)
            half_day = 1
            total_hours = hours//2
        case 2:
            total_wage = 0
            absent = 1
    return full_day, half_day, absent, full_day+half_day, total_hours, total_wage

# function to calculate the monthly wage of an employee for either 20 days or 100 hours
def calculate_monthly_wage():
    no_of_days = total_working_hrs = total_full_days = total_half_days = total_absent_days = total_monthly_wage = 0
    # loop untill no of days is 20 or total hours is and
    while no_of_days < 20 and total_working_hrs < 100:
        temp = calculate_daily_wage()
        total_full_days += temp[0]
        total_half_days += temp[1]
        total_absent_days += temp[2]
        no_of_days += temp[3]
        total_working_hrs += temp[4]
        total_monthly_wage += temp[5]
  
    return total_full_days, total_half_days, total_absent_days, no_of_days,total_working_hrs, total_monthly_wage # returns a tuple containing total full days, half days, absent days, total working hours, total working days and monthly wage

# main method
def main():
    result = calculate_monthly_wage()
    print("\n***Employee Wage***\n")
    print(f"Total number of full days: {result[0]}\n\nTotal number of half days: {result[1]}\n\nTotal number of absent days: {result[2]}\n\nTotal number of working days {result[3]}\n\nTotal working hours: {result[4]}\n\nThe total wage for the month is Rs.{result[5]}/-\n")


if __name__=="__main__":
    main()
    
