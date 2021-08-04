# DATETIMES

# Representing time with datetimes
# Python standard library includes the datetime module that provides useful functionaliy 
from datetime import datetime
# Datetime objects have attributes representing year, month, date, hour, minute, second, microsecond and timezone
black_monday = datetime(1987, 10, 19) # at least provide year, month, date
print(black_monday) # market crash date in 1987
# Creating datetimes for dates
flash_crash = datetime(1962, 5, 28)
print(flash_crash)
# Datetime now
now = datetime.now()
print(now)
# Datetime from string
black_monday_str = "Monday, October 19, 1987. 9:30 am"
format_str = "%A, %B %d, %Y. %I:%M %p"
datetime.strptime(black_monday_str, format_str)
# String from datetime
great_depression_crash = datetime(1929, 10, 29)
print(great_depression_crash)
great_depression_crash.strftime("%a, %b %d, %Y")
# Format strings for mapping datetimes can be found at strftime.org
crash_text = "Friday the 13th, Oct, 1989" # mini crash in 1989
crash_format_str = "%A the %dth, %b, %Y"
min_crash = datetime.strptime(crash_text, crash_format_str)
print(min_crash)
# Construct a format string that maps to the text for the recession of 1990
recession_text = "07/03/90"
recession_format_str = "%m/%d/%y"
recession = datetime.strptime(recession_text, recession_format_str)
print(recession)
# Converting format with datetimes
org_text = "Sep 16 1992"
org_format = "%b %d %Y"
black_wednesday = datetime.strptime(org_text, org_format)
print(black_wednesday)
# New format: "Wednesday, September 16, 1992"
new_format = "%A, %B %d, %Y"
new_text = black_wednesday.strftime(new_format)
print(new_text)

# Working with datetimes
# Dateime attributes
now.year
now.month
now.day
now.hour
now.minute
now.second
# Accessing datetime attributes
tech_bubble = datetime(2000, 3, 10)
yr = tech_bubble.year
mth = tech_bubble.month
day = tech_bubble.month
print(f"Year: {yr}, Month: {mth}, Day: {day}")
# Compare datetimes
asian_crisis = datetime(1997, 7, 2)
world_mini_crash = datetime(1997, 10, 27)
# See which event came first
asian_crisis > world_mini_crash
asian_crisis < world_mini_crash # smaller date means event that happens first
# Create another datetime object with the same date
text = "10/27/1997"
format_str = "%m/%d/%Y"
sell_date = datetime.strptime(text, format_str)
sell_date == world_mini_crash
# Differences between datetimes: timedelta object
delta = world_mini_crash - asian_crisis
type(delta)
# Access the differences between two datetimes by acessing its attributes
delta.days
# Create relative datetimes
from datetime import timedelta
offset = timedelta(weeks = 1)
offset
now - offset
# timedelta manages crossing temporal boundaries
offset = timedelta(days = 16)
now - offset
# The Troubled Asset Relief Program (TARP) was passed in October of 2008 
tarp = datetime(2008, 10, 3)
# One week before TARP was passed
week_before = tarp - timedelta(days = 7)
print(week_before)