import datetime
from datetime import date, timedelta

schedule = {
   "timeZone" : "+5:30",
   "startDate" : ("2021-02-01T00:00:00.000Z"),
   "endDate" : ("2021-02-10T00:00:00.000Z"),
   "businessHours" : {
       "startTime" : "03:30",
       "endTime" : "12:30",
       "format" : "24 hours",
       "durationInHours" : 3,
       "includeWeekends" : True,
       "includeHolidays" : True
   },
   "breakHours" : [
       {
           "startTime" : "07:30",
           "endTime" : "08:30",
           "format" : "24 hours",
           "durationInHours" : ""
       }
   ],
   "holidays" : [{"startDate" : ("2021-02-01T00:00:00.000Z"),
                  "endDate" : ("2021-02-08T00:00:00.000Z")}],
   "weekends" : [
       "Saturday",
       "Sunday"
   ],
   "slots": [
    {
    "dateID": "",
    "date": "2021-01-28T00:00:00.000Z",
    "timings": [{"timeID": "", "startTime" : "03:00", "endTime" : "17:00"}]
    }
   ]

}

def prepare_slots(schedule):
    #changes need to be done in slots method  it only works if we have only one slot i ah day  
    def slots(list,weekend,holidays): #here we are removing weekdays from slots
        slot = []
        for  i in range(len(list)):
            if (list[i][1]  not in weekend) & ( list[i][2] not in holidays):
                slot.append({"dateID": "",
                "date" : list[i][2]+"T00:00:00.000Z",
                "timings": [{"timeID": "","startTime" : list[i][0][0], "endTime" :  list[i][0][1]}]
                })
        return slot
    def find_slots(stime,etime,start_date,end_date,slot_time):
        days = []
        date = start_date
        while date <= end_date:
            year,month,day = str(date).split('-')[0],str(date).split('-')[1],str(date).split('-')[2] #added by me
            d =  datetime.date(int(year),int(month),int(day))
            tempd = date.strftime("%Y-%m-%d")
            hours = []
            time = datetime.datetime.strptime(stime, '%H:%M')
            end = datetime.datetime.strptime(etime, '%H:%M')
            while time <= end:
                hours.append(time.strftime("%H:%M"))
                time += datetime.timedelta(minutes=slot_time)
            date += datetime.timedelta(days=1)
            days.append([hours,d.strftime("%A"),tempd ])
        return days
    #dates
    sy,sm,sd =int(schedule["startDate"].split('-')[0]),int(schedule["startDate" ].split('-')[1]),int(schedule["startDate" ].split('-')[2].split('T')[0])
    ey,em,ed =int(schedule["endDate"].split('-')[0]),int(schedule["endDate" ].split('-')[1]),int(schedule["endDate" ].split('-')[2].split('T')[0])
    start_date = datetime.datetime(sy,sm,sd).date()
    end_date = datetime.datetime(ey,em,ed).date() 
    #non workings
    weekend = schedule["weekends"] 
    #time section
    start_time = schedule["businessHours"]["startTime"]
    end_time = schedule["businessHours"]["endTime"]
    slot_time  = schedule["businessHours"]["durationInHours"]*60 # taking in mins
    break_start =  schedule["breakHours"][0]["startTime"]
    break_end =  schedule["breakHours"][0]["endTime"] 
        
    #holidays section
    sdate = date(int(schedule["holidays"][0]["startDate"].split('-')[0]),int(schedule["holidays"][0]["startDate" ].split('-')[1]),int(schedule["holidays"][0]["startDate" ].split('-')[2].split('T')[0]))  # start date
    edate = date(int(schedule["holidays"][0]["endDate"].split('-')[0]),int(schedule["holidays"][0]["endDate"].split('-')[1]),int(schedule["holidays"][0]["endDate"].split('-')[2].split('T')[0]))  # end date

    delta = edate - sdate       # as timedelta
    holidays = []
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        holidays.append(str(day))
  

    #slots get splitted to before time and after time
    # before break
    before_b= find_slots(start_time,break_start,start_date,end_date,slot_time) 
    main_slots = slots(before_b, weekend,holidays)
    # after break
    after_b = find_slots(break_end,end_time,start_date,end_date,slot_time) 
    slots_after_break = slots(after_b, weekend, holidays)

    for i in slots_after_break:
        main_slots.append(i)

    return main_slots











