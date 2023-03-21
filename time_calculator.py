def add_time(start, duration, startDay=None):
    start = start.split(" ")
    start[0] = start[0].split(":")

    totalMinutesStart = int(start[0][0])*60+int(start[0][1])
    if start[1] == "PM":
        totalMinutesStart += 720
    
    duration = duration.split(":")
    totalMinutesAdd = int(duration[0])*60+int(duration[1])

    totalMinutesEnd = totalMinutesStart + totalMinutesAdd

    days = 0
    while totalMinutesEnd>1440:
        totalMinutesEnd-=1440
        days+=1

    endHour = int(totalMinutesEnd/60)
    if endHour < 12:
        midDay = " AM"
        if endHour == 0:
            endHour = 12
    elif endHour == 12:
        midDay = " PM"
    else:
        midDay = " PM"
        endHour-=12
    
    endMinute = totalMinutesEnd%60

    if startDay != None:
        startDay = startDay.lower()
        weekDays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        newDayIndex = weekDays.index(startDay) + days
        while newDayIndex > 6:
            newDayIndex -= 6
        newDay = ", " + str(weekDays[newDayIndex]).capitalize()
    else:
        newDay = ""
    
    if days == 0:
        days = ""
    elif days == 1:
        days = " (next day)"
    else:
        days = " ({passedDays} days later)".format(passedDays = days)
    
    endHour = str(endHour)
    if endMinute < 10:
        endMinute = "0" + str(endMinute)
    endMinute = str(endMinute)
    new_time = endHour + ":" + endMinute + midDay + newDay + days

    return new_time