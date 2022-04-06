import datetime
import time


def NowStr():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def NowStamp():
    return time.localtime(time.time())

def CalDeltaSecond(EndStr, StartStr):
    start = datetime.datetime.strptime(StartStr, "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(EndStr, "%Y-%m-%d %H:%M:%S")
    return (end - start).total_seconds()

