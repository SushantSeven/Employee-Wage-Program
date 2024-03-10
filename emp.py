import random

# method to check attendance of an employee
def attendance(flag):
    return f"Employee is present!" if flag == 0 else f"Employee is absent!"

# main method to drive other methods
def main():
    print(attendance(random.randint(0,1)))

if __name__=="__main__":
    main()
    

