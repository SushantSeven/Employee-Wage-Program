import random

def check_attendance():
    check_attd = random.randint(0,1)
    if check_attd == 1:
        return f"The employee is present.", calculate_daily_wage(check_attd)
    else:
        return f"The employee is absent.", calculate_daily_wage(check_attd)

def calculate_daily_wage(check_att):
    wage = 20
    hrs = 8
    return f"The wage of employee is {wage*hrs}Rs. " if check_att == 1 else f"The wage of employee is 0 Rs. "


if __name__=="__main__":
    result = check_attendance()
    print("\n".join(result))
    
                    