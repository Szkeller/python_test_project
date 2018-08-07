import time
import calenar
# get the local time
localtime = time.asctime(time.localtime(time.time()))
print("local time is: ", localtime)

# get the calendar month by given year and month
cal = calendar.month(2017, 11)
# print "Sept 2017:"
print(cal)
