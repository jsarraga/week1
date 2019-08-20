#!/usr/bin/env python3
import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
daysLeft = currentDate - deadlineDate 
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)
print(years)
print(yearsInt)

months=(years)*12
monthsInt=int(months)

days=(monthsInt)*(365.242/12)
daysInt=int(days)

hours = (daysInt)*24
hoursInt=int(hours)

minutes = (hoursInt)*60
minutesInt=int(minutes)

seconds = (minutesInt)*60
secondsInt =int(seconds)

print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))