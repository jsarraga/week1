def age_to_time(x):
    months = x * 12
    days = x * 365
    hours = x * 8760
    minutes = x * 525600

    print(months, ' months')
    print(days, ' days')
    print(hours, ' hours')
    print(minutes, ' minutes')


age_to_time(18)