import random

def welcome_message():
    print("Welcome to Employee Wage Computation Program")

def check_attendance():
    return random.choice(["Present", "Absent"])

if __name__ == "__main__":
    welcome_message()
    print(f"Employee is {check_attendance()}")
