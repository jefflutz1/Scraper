import datetime

currentTime = datetime.datetime.now()

allTimes = []

for x in range(10):
    allTimes.append(currentTime - datetime.timedelta(seconds=x*20))