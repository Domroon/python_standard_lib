from datetime import datetime as DateTime
from datetime import datetime, timezone, timedelta, tzinfo

now = DateTime.now()
print(f'now: {now}')

date = now.date()
print(f'date: {date}')

time = now.time()
print(f'time: {time}')

timetz = now.timetz()
print(f'timetz: {timetz}')

utcoffset = now.utcoffset()
print(f'utcoffset: {utcoffset}')

timetuple = now.timetuple()
print(f'timetuple: {timetuple}')

utctimetuple = now.utctimetuple()
print(f'utctimetuple: {utctimetuple}')

timestamp = now.timestamp()
print(f'timestamp: {timestamp}')

weekday = now.weekday()
print(f'weekday: {weekday}')

isoweekday = now.isoweekday()
print(f'isoweekday: {isoweekday}')

isocalendar = now.isocalendar()
print(f'isocalendar: {isocalendar}')

isoformat = now.isoformat()
print(f'isoformat: {isoformat}')

example = datetime(2019, 5, 18, 15, 17, tzinfo=timezone.utc).isoformat()
print(f'example: {example}')

class TZ(tzinfo):
    """A time zone with an arbitrary, constant -06:39 offset."""
    def utcoffset(self, dt):
        return timedelta(hours=-6, minutes=-39)

print(datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' '))
print(datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat())

ctime = now.ctime()
print(f'ctime: {ctime}')

strftime = now.strftime("%A, %d.%B %Y %T %Z")
print(f'strftime: {strftime}')