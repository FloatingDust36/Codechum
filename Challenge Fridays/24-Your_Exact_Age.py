from datetime import datetime
import calendar

m = int(input("Enter month number: "))
d = int(input("Enter day: "))
y = int(input("Enter year: "))
h = int(input("Enter hour: "))
min_val = int(input("Enter minute: "))

# Fetch the exact current time from the judge's server
now = datetime.now()

# Step 1: Initial raw subtraction
years = now.year - y
months = now.month - m
days = now.day - d
hours = now.hour - h
minutes = now.minute - min_val

# Step 2: "Borrowing" logic for negative values
if minutes < 0:
    minutes += 60
    hours -= 1

if hours < 0:
    hours += 24
    days -= 1

if days < 0:
    months -= 1
    # To borrow days, we need to know exactly how many days were in the *previous* month
    prev_month = now.month - 1 if now.month > 1 else 12
    prev_year = now.year if now.month > 1 else now.year - 1

    # calendar.monthrange returns (weekday, number_of_days)
    _, days_in_prev_month = calendar.monthrange(prev_year, prev_month)
    days += days_in_prev_month

if months < 0:
    months += 12
    years -= 1

print(
    f"You have lived for {years} years, {months} months, {days} days, {hours} hours, and {minutes} minutes.")
