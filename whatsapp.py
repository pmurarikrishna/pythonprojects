from datetime import datetime
from datetime import timedelta
import pywhatkit 

now=datetime.now()
gap=timedelta(minutes=4)
nextTime=now+gap
print(now)
print(nextTime)
hour=nextTime.hour
min=nextTime.minute
print(hour," : ",min)
pywhatkit.sendwhatmsg('+7249373220', 'HELLO, HOW ARE YOU?', hour,min,10) 