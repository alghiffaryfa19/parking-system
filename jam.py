import datetime 
  
# datetime(year, month, day, hour, minute, second) 
a = datetime.datetime(2017, 6, 21, 18, 25, 30) 
b = datetime.datetime(2017, 5, 16, 8, 21, 10) 
  
# returns a timedelta object 
c = a-b  
print('Difference: ', c) 
  
minutes = c.total_seconds() / 3600
print('Total difference in minutes: ', minutes) 
  
# returns the difference of the time of the day 
minutes = c.seconds / 3600
print('Difference in minutes: ', minutes) 