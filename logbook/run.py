from datetime import datetime
from datetime import timedelta


class eventdetail:
    opentimestamp = None
    closetimestamp = None

    def __init__(self, opentime):
        self.opentimestamp = opentime

    def addclose(self, closetime):
        if self.closetimestamp is not None:
            raise Exception("Already closed")
        self.closetimestamp = closetime

    # getting time difference in seconds

    def gettimedelta(self):
        if self.closetimestamp is None:
            return 0
        else:
            timediff = self.closetimestamp - self.opentimestamp
            return int(timediff.total_seconds())


# converts to datetime field

def gettime(month, day, time_val):
    return datetime.strptime(month + " " + day + " " + time_val, '%b %d %H:%M:%S:%f')

# converts datetime field to string


def getdatestr(timestamp):
    string = timestamp.strftime('%b %d %H:%M:%S:%f')
    print("   {}".format(string))


# ----------------------------------------------------
# READING FROM THE TEST FILE


with open("logs.txt") as logfile:
    data = logfile.readlines()
    logfile.close()

# INITIALISING VARS

events = {}
event_obj = []
error_events = []


for line in data:
    details = line.split()
    device_name = details[3]
    device_name = device_name[1:-1]

    if details[-1] == 'ON':
        obj = eventdetail(gettime(details[0], details[1], details[2]))
        events[device_name] = len(event_obj)
        event_obj.append(obj)
        error_events.append(list())

    elif details[-1] == 'ERR':
        pos = events.get(device_name)
        error_events[pos].append(gettime(details[0], details[1], details[2]))

    else:
        pos = events.get(device_name)
        if pos is not None:
            event_obj[pos].addclose(
                gettime(details[0], details[1], details[2]))


# DATA OUTPUT

for key, val in (events).items():
    obje = event_obj[val]
    error_list = error_events[val]
    print("Device {} was on for {} seconds".format(key, obje.gettimedelta()))
    if len(error_list) == 0:
        print("Device {} had no error events.\n".format(key))
    else:
        print("Device {} had the following error events:".format(key))
        for item in error_list:
            getdatestr(item)
