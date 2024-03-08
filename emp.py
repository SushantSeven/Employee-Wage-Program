import random

def attendance(flag):
    return f"Employee is present!" if flag == 0 else f"Employee is absent!"


if __name__=="__main__":
    print(attendance(random.randint(0,1)))

