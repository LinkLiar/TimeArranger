import datetime
import time


def Now(type="stamp"):
    if(type == "str"):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    else:
        return time.localtime(time.time())


def CalDelta(end, start):

    if(type(end) == str and type(start) == str):
        start = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
        return (end - start).total_seconds()
    else:
        return end - start
