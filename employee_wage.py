import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

def welcome_message():
    print("Welcome to Employee Wage Computation Program")

def check_attendance():
    return random.choice(["Present", "Absent"])

def calculate_daily_wage(hours):
    return hours * WAGE_PER_HOUR

if __name__ == "__main__":
    welcome_message()
    attendance = check_attendance()
    if attendance == "Present":
        daily_wage = calculate_daily_wage(FULL_DAY_HOUR)
        print(f"Daily Wage: {daily_wage}")
    else:
        print("No wage, employee is absent")
