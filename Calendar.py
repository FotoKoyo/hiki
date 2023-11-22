import calendar
import datetime as dt

date = dt.datetime.now()
days = []
mm = date.month
year = date.year
a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')

with open('calendar.html', 'w') as g:
    print(a.formatyear(year, width=4), file=g)