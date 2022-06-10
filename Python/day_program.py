from datetime import date
import calendar
from multiprocessing.dummy import current_process
current_date = date.today()
#print ( calendar.day_name[current_date.weekday()])
#DAY = date.today().weekday()
DAY= ( calendar.day_name[current_date.weekday()])
print (DAY)
if DAY == "Monday":
    print ("Have fun")
elif DAY == "Tuseday":
    print ("Hang on in there!")
elif DAY == "Wednesday":
    print ("You're half way thourg the week")
else:
    print ("It's almost the weekend!")