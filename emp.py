import random

# a class named Employee_wage is created
class Employee_wage:
    
# init method to initialize the class variables
    def __init__(self):
        
        self.wage = 20
        self.hours = 8

# function to check the attendance of an employee
    def check_attendance(self):  
        check_attd = random.randint(0,2)
        return check_attd

# function to calculate the daily wage of an employee       
    def calculate_daily_wage(self):
        full_day = half_day = absent = total_hours= 0
        presence = self.check_attendance()
        match presence:
            case 0:
                total_wage = self.wage * self.hours
                full_day = 1
                total_hours = self.hours
            case 1:
                total_wage = self.wage * (self.hours/2)
                half_day = 1
                total_hours = self.hours//2
            case 2:
                total_wage = 0
                absent = 1
        return full_day, half_day, absent, full_day+half_day, total_hours, total_wage

# function to calculate the monthly wage of an employee for either 20 days or 100 hours
    def calculate_monthly_wage(self):
        no_of_days = total_working_hrs = total_full_days = total_half_days = total_absent_days = total_monthly_wage = 0
        while no_of_days < 20 and total_working_hrs < 100:
            temp = self.calculate_daily_wage()
            total_full_days += temp[0]
            total_half_days += temp[1]
            total_absent_days += temp[2]
            no_of_days += temp[3]
            total_working_hrs += temp[4]
            total_monthly_wage += temp[5]
    
        return total_full_days, total_half_days, total_absent_days, no_of_days,total_working_hrs, total_monthly_wage

# main method
def main():
    employee_1 = Employee_wage().calculate_monthly_wage() # intance of the Employee_wage class is created and function to calculate monthly wage is called
    print(f"\nTotal number of full days: {employee_1[0]}\n\nTotal number of half days: {employee_1[1]}\n\nTotal number of absent days: {employee_1[2]}\n\nTotal number of working days {employee_1[3]}\n\nTotal working hours: {employee_1[4]}\n\nThe total wage for the month is Rs.{employee_1[5]}/-\n")


if __name__=="__main__":
    main()
    