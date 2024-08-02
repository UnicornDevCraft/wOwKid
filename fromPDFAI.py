fromFile = 'january_rus.txt'
dayBorn, dayDied, holiday = '', '', ''
monthBorn, monthDied, monthHoliday = '', '', ''
yearBorn, yearDied = '', ''
holidays = []
dateBorn, dateDied = [], []
with open(fromFile, 'r') as f:
    for line in f.readlines()[2:]:
        items = line.split('|')
        dates = items[1].split()
        if '-' not in dates:
            holiday = dates[0]
            monthHoliday = dates[1]
            holidays.append(holiday + ' ' + monthHoliday)
        elif '-' in dates:
            dayBorn = dates[0]
            monthBorn = dates[1]
            yearBorn = dates[2]
            dayDied = dates[4]
            monthDied = dates[5]
            yearDied = dates[6]
            dateBorn.append(dayBorn + ' ' + monthBorn + ' ' + yearBorn)
            dateDied.append(dayDied + ' ' + monthDied + ' ' + yearDied)
        else:
            print('Need to check this:', dates)
print(holidays)
print(dateBorn)
print(dateDied)
