import random

# a class named Employee_wage is created
class Employee_wage:
    
# init method to initialize the class variables
    def __init__(self):    
        self.hours = 8

# function to check the attendance of an employee
    def check_attendance(self):  
        check_attd = random.randint(0,2)
        return check_attd
    
# function to calculate the daily wage of an employee
    def calculate_daily_wage(self, per_day_wage):
        full_day = half_day = absent = total_hours= 0
        presence = self.check_attendance()
        match presence:
            case 0:
                total_wage = per_day_wage * self.hours
                full_day = 1
                total_hours = self.hours
            case 1:
                total_wage = per_day_wage * (self.hours/2)
                half_day = 1
                total_hours = self.hours//2
            case 2:
                total_wage = 0
                absent = 1
        return full_day+half_day, total_hours, total_wage

# function to calculate the monthly wage of an employee for either 20 days or 100 hours
    def calculate_monthly_wage(self, total_working_days, total_working_hrs, per_day_wage):
        t_w_d = t_w_h = total_monthly_wage = 0
        while t_w_d < total_working_days and t_w_h < total_working_hrs:
            temp = self.calculate_daily_wage(per_day_wage)
            t_w_d += temp[0]
            t_w_h += temp[1]
            total_monthly_wage += temp[2]
    
        return t_w_d, t_w_h, total_monthly_wage


if __name__=="__main__":
    employee_1 = Employee_wage().calculate_monthly_wage(20, 100, 200) # instnce of Employee class is made and monthly working hours, working days and wage per day is passed to the calculate_monthly_wage method according to a specific company
    print(f"\nNumber of working days of employee: {employee_1[0]} days\n\nNumber of working hours: {employee_1[1]} hrs\n\nMonthly wage: Rs.{employee_1[2]}\n")
   