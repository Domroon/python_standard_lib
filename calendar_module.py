import calendar

cal = calendar.Calendar()

print('\nweekdays:')
for weekday in cal.iterweekdays():
    print(weekday)

print('\nmonthdates for 2021/11:')
for monthdate in cal.itermonthdates(2021, 11):
    print(monthdate)

print('\nmonthdayscalendar for 2021/11:')
print(cal.monthdayscalendar(2021, 11))

# print('yeardatescalendar for 2021')
# print(cal.yeardatescalendar(2021))


text_cal = calendar.TextCalendar()

print('\nformatmonth for 2021/11:')
print(text_cal.formatmonth(2021, 11))

print('\nformatyear for 2021')
print(text_cal.formatyear(2021))


html_cal = calendar.HTMLCalendar()
print('\nformatmonth for 2021/11')
print(html_cal.formatmonth(2021, 11))

print('\n is 2021 a leap year?')
print(calendar.isleap(2021))

print('\n leap years between 1994 and 2021:')
print(calendar.leapdays(1994, 2021))