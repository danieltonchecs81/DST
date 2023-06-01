'''
#Displays current time
#Testing which code will run on my DST project
#Must display time in this format
#12:00 am - 11:59 am
#12:00 pm - 11:59 pm
#Write a code that subtracts time by 1 hour
'''

##This code displays time, not a good format don't use
import datetime
TodayDate = datetime.datetime.now()
print(TodayDate)

##Display Month, Day and Year
import datetime
TodayDate = datetime.datetime.now()
Year = TodayDate.strftime('%Y')
Month = TodayDate.strftime('%m')
Day = TodayDate.strftime('%d')
FormattedDate = Month + '/' + Day + '/' + Year #'/' keeps date organized
print(FormattedDate)

##^Example what this ^code^ displays 05/18/2023

##This code displays time in this format 24:00:00
import datetime
TodayDate = datetime.datetime.now()
Hour = TodayDate.strftime('%H')
Minute = TodayDate.strftime('%M')
Second = TodayDate.strftime('%S')
t24 = Hour + ':' + Minute + ':' + Second
print(t24)

##This code displays time in this format AM and PM
import datetime
TodayDate = datetime.datetime.now()
Hour = TodayDate.strftime('%I')
Minute = TodayDate.strftime('%M %p')
t12 = Hour + ':' + Minute
print(t12)

##This code displays time in Standard Time
#Note- this code will display wrong hour when Standard Time is active
from datetime import datetime
from datetime import timedelta
today = datetime.today()
yesterday = today - timedelta(hours=1)

print()
print(yesterday)



