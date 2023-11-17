#program that prints current date ant time

from datetime import datetime

date_time = datetime.now()

print(f"the current time is {date_time}")

# specifying a particular format

# Get the current date and time
current_date_time = datetime.now()

# Extract the time (hours and minutes)
time_only = current_date_time.strftime("%H:%M")  # Format for hours and minutes

# Print only the time (hours and minutes)
print("Current Time (Hours and Minutes):", time_only)
