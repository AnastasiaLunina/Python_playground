# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.

age = input("What is your current age?")

age_int = int(age)
years_remaining = 90 - age_int
x_days = float(years_remaining * 365)
y_weeks = int(years_remaining * 52)
z_month = int(years_remaining * 12)

print(f"You have {x_days} days, {y_weeks} weeks, and {z_month} months left.")




