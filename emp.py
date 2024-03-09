import random

# wage and working hours are declared globaly
wage = 20
hours = 8

# function to check the attendance of an employee
def check_attendance():
    check_attd = random.randint(0,2) # variable that holds the random choice to check attendance
    if check_attd == 0:
        return f"The employee is present full day.", check_attd # if 0 than employee is present full day 
    elif check_attd ==1:
        return f"The employye is present half day.", check_attd # if 1 than employee is present half day
    else:
        return f"The employee is absent.", check_attd # if 2 than employee is absent

# function to calculate the daily wage of an employee   
def calculate_daily_wage():
    presence = check_attendance() # check_attendance method is called
    if presence[1] ==0:
        total_wage = wage * hours # total wage is calculated
    elif presence[1] == 1:
        total_wage = wage * (hours/2)
    else:
        total_wage = 0
    return presence[0] , str(total_wage) # the total wage and whether the employee is present of absent is r returned


if __name__=="__main__":
    result = calculate_daily_wage()
    print(f"\n{result[0]} \n\nThe total wage for the day is Rs.{result[1]}/-\n")
   
    
