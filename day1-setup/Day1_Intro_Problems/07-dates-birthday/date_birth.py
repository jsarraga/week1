#!/usr/bin/env python3
import datetime
age = int(input("How old are you?"))
def age_to_time(age):
    months = age * 12
    days = int(months * (365.242/12))
    hours = age * 8760
    minutes = age * 525600

    print(months, ' months')
    print(days, ' days')
    print(hours, ' hours')
    print(minutes, ' minutes')




deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')

def birthday_to_time(deadline):

    currentDate = datetime.datetime.now()

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