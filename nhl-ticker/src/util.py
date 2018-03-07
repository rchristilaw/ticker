from datetime import datetime
from dateutil import tz
import pytz

def convertUtcDateTimeToLocal(utcTime):
    
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = datetime.strptime(utcTime, '%Y-%m-%dT%H:%M:%SZ')

    utc = utc.replace(tzinfo=from_zone)
    localTime = utc.astimezone(to_zone)

    return localTime

def isBeforeCurrentTime(time):
    return time < pytz.utc.localize(datetime.now())