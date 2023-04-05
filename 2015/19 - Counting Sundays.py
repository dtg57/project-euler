import datetime

def upmonth(date):
    if date.month==12:
        date=datetime.date(date.year+1,1,1)
    else:
        date=datetime.date(date.year,date.month+1,1)
    return date

def getall(start,end):
    days=[]
    test=datetime.date(start,1,1)
    for i in range(((end-start)+1)*12):
        if test.weekday()==6:
            days.append(test)
        test=upmonth(test)
    return days
    
print (len(getall(1901,2000)))
            
